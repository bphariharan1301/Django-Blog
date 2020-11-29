from os import name
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from . import views

# from . import views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserUpdateView.as_view(), name='edit_profile'),
    path('password/', PasswordsUpdateView.as_view(), name='change-password'),
    path('password_success', views.password_success, name='password_success'),
]