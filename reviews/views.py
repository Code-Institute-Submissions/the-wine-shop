from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Product, WineOrigin, WineColour
from .forms import ReviewForm


@login_required
def add_review(request):
    """ Add review to the product """

    # If the user is not a superuser send them back to the homepage
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you must have purchased something to do this.')
        return redirect(reverse('home'))

    # If request method is post, instantiate new instance of the review form
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        # If form is valid, save it and redirect user to add review view
        if form.is_valid():
            review = form.save()
            messages.success(request, 'Review added successfully')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            # If there are errors on the form...
            messages.error(request, 'Cannot add review - please ensure the form is completed properly')
    else:
        form = ReviewForm()

    template = 'reviews/add_review.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
