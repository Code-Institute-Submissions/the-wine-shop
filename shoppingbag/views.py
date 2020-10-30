from django.shortcuts import render, redirect, reverse, HttpResponse


def view_bag(request):
    """ Return the shopping bag page """

    return render(request, 'bag/bag.html')


def add_to_shoppingbag(request, item_id):
    """ Add chosen products to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    shoppingbag = request.session.get('shoppingbag', {})

    if item_id in list(shoppingbag.keys()):
        shoppingbag[item_id] += quantity
    else:
        shoppingbag[item_id] = quantity

    request.session['shoppingbag'] = shoppingbag
    return redirect(redirect_url)


def amend_shoppingbag(request, item_id):
    """ Amend products in the shopping bag """

    quantity = int(request.POST.get('quantity'))
    shoppingbag = request.session.get('shoppingbag', {})

    if quantity > 0:
        shoppingbag[item_id] = quantity
    else:
        shoppingbag.pop[item_id]

    request.session['shoppingbag'] = shoppingbag
    return redirect(reverse('view_bag'))


def remove_from_shoppingbag(request, item_id):
    """Remove item from the shopping bag"""

    try:
        shoppingbag = request.session.get('shoppingbag', {})

        shoppingbag.pop(item_id)

        request.session['shoppingbag'] = shoppingbag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
