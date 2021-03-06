from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderContents

from profiles.forms import UserProfileForm
from profiles.models import UserProfile

from products.models import Product
from shoppingbag.contexts import shoppingbag_contents

import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'save_info': request.POST.get('save_info'),
            'shoppingbag': json.dumps(request.session.get('shoppingbag', {})),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry your payment cannot be  \
            processed at this time. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        shoppingbag = request.session.get('shoppingbag', {})

        form_data = {
            'forename': request.POST['forename'],
            'surname': request.POST['surname'],
            'email': request.POST['email'],
            'phone': request.POST['phone'],
            'address1': request.POST['address1'],
            'address2': request.POST['address2'],
            'town': request.POST['town'],
            'county': request.POST['county'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_shoppingbag = json.dumps(shoppingbag)
            order.save()
            for item_id, item_data in shoppingbag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderContents(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag is unavailable. "
                        "Please contact us for assistance.")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form,  \
            please check your information.')
    else:
        shoppingbag = request.session.get('shoppingbag', {})
        if not shoppingbag:
            messages.error(request, "Your bag is empty")
            return redirect(reverse('products'))

        current_bag = shoppingbag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        # If user is authenticated, get their profile info and use it on their order form
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    # from user account
                    'forename': profile.user.first_name,
                    'surname': profile.user.last_name,
                    'email': profile.user.email,
                    # from default info in profile
                    'phone': profile.default_phone_number,
                    'town': profile.default_town,
                    'address1': profile.default_address1,
                    'address2': profile.default_address2,
                    'county': profile.default_county,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing.  \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """ Handle successful checkouts"""
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'default_phone_number': order.phone,
                'default_town': order.town,
                'default_address1': order.address1,
                'default_address2': order.address2,
                'default_county': order.county,
                'default_country': order.country,
                'default_postcode': order.postcode,
            }
            # Create an instance of the user profile form using the profile data
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            # If the form is valid, save it
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Order processed successfully.  \
        Your order number is {order_number}. A confirmation  \
        email will be sent to {order.email}.')

    if 'shoppingbag' in request.session:
        del request.session['shoppingbag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
