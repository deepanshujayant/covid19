from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Corona

class OrderForm(ModelForm):
    class Meta:
        model = Corona
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name', 'email', 'password1', 'password2']