from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, WineOrigin, WineColour
from .forms import ProductForm


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


def add_product(request):
    """ Add product to the store """

    # If request method is post, instantiate new instance of the product form
    # and include request.files so as to capture the image if one is submitted
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        # If form is valid, save it and redirect user to add product view
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully')
            return redirect(reverse('add_product'))
        else:
            # If there are errors on the form...
            messages.error(request, 'Cannot add product - please ensure the form is completed properly')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


# View to edit product which takes the id of the product to be edited
def edit_product(request, product_id):
    """ Edit a product in the store """

    # get the product
    product = get_object_or_404(Product, pk=product_id)

    # If request method is post, instantiate new instance of the product form
    # and include request.files so as to capture the image if one is submitted
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        # If form is valid, save it and redirect user to product detail page
        if form.is_valid():
            form.save()
            messages.success(request, 'Product edited successfully')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            # If there are errors on the form...
            messages.error(request, 'Cannot edit product - please ensure the form is completed properly')
    else:
        # instantiate/prefill the form
        form = ProductForm(instance=product)
        # message to tell the user they're editing a product
        messages.info(request, f'You are editing {product.name}')

    # which template to use
    template = 'products/edit_product.html'
    # template context with form and product in it
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)
