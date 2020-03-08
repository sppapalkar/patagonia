from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm


def home(request):
    return render(request, 'users/home.html')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('first_name')
            messages.success(request, f'Account created for {username}!')
            return redirect('users-home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})
