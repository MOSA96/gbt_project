from django.shortcuts import render
from .models import User, Dish, Ingredient

def index(request):
    """View function for home page"""
    num_user = User.objects.all().count()

    context = {
        'num_user': num_user,
    }
    return render(request, 'index.html', context=context)


def dishes(request):
    return render(request, 'mydishes.html')


def add_dish(request):
    return render(request, 'add_dish.html')