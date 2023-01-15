from django.shortcuts import render
from .models import Item


def index(request):
    """ A view to return the index page """

    return render(request, 'oaksmokebakery/index.html')


def aboutus(request):
    """ A view to return the about page """

    return render(request, 'oaksmokebakery/about.html')


def item_list(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'oaksmokebakery/items_list.html', context)