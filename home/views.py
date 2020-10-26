from django.shortcuts import render


def index(request):
    """ Return the index page """

    return render(request, 'home/index.html')
