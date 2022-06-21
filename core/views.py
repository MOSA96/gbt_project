from django.shortcuts import render, redirect
from dishes.models import User
from django.contrib.auth import authenticate, login, logout


#Core views
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


#Log In views
def signup(request):
    return render(request, 'signup.html')


def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(request, username=username, password=password )
            if user is not None and user.is_active and user.check_password:
                login(request, user)
                return redirect('home')
            else:
                login_errors = 'Invalid User or Password'
                return render(request, 'login.html', {'login_erros': login_errors})
        else:
            if request.user and request.user.is_authenticated:
                return redirect('home')

    return render(request, 'login.html')


def logout(request):
    if request.user:
        logout(request)
    return redirect('home')