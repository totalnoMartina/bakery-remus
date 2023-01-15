from django.shortcuts import render


def index(request):
    """ A view to return the index page """

    return render(request, 'oaksmokebakery/index.html')


def aboutus(request):
    """ A view to return the about page """

    return render(request, 'oaksmokebakery/about.html')