from django.shortcuts import render
from dishes.models import User


def home(request):
    """View function for home page"""
    num_user = User.objects.all().count()

    context = {
        'num_user': num_user,
    }
    return render(request, 'home.html', context=context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')