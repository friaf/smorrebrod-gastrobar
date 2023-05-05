from django.shortcuts import render
from .models import Item


def menupage(request):
    best_menu = Item.objects.all()
    context = {
        'best_menu': best_menu
    }
    return render(request, 'menu.html', context=context)