from django.shortcuts import render, redirect


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
