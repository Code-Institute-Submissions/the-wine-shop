from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    shoppingbag = request.session.get('shoppingbag', {})
    if not shoppingbag:
        messages.error(request, "Your bag is empty")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Hi11YJDq1AhGiGdMZoDROywpgyalmziyK7LtaKIHMsCepNGWUIMSKm6rne62cjROQnE3R6gkSaZpkqfUv5e3h2G00cvNJ2669',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
