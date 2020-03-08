from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib import messages
# from .forms import CustomUserCreationForm


def home(request):
    return render(request, 'users/home.html')




