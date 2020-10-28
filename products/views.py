from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, WineOrigin, WineColour


def all_products(request):
    """ Return all products, search and filter for products """

    products = Product.objects.all()
    query = None
    origins = None
    colours = None

    if request.GET:
        if 'origin' in request.GET:
            origins = request.GET['origin'].split(',')
            products = products.filter(origin__origin__in=origins)
            origins = WineOrigin.objects.filter(origin__in=origins)

        if 'colour' in request.GET:
            colours = request.GET['colour'].split(',')
            products = products.filter(colour__colour__in=colours)
            colours = WineColour.objects.filter(colour__in=colours)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter something in the search box")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_origins': origins,
        'current_regions': colours,
    }

    return render(request, 'products/products.html', context)


def product_details(request, product_id):
    """ Return individual product """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_details.html', context)
