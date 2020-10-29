from django.shortcuts import render


def view_bag(request):
    """ Return the shopping bag page """

    return render(request, 'bag/bag.html')
