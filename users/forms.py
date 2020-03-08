from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.TextInput()
    last_name = forms.TextInput()

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name','email']
