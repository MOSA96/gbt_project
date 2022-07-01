from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.loginview, name='login'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('profile/', views.user_profile, name='user_profile')
]