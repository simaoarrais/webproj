from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    attrs = {
        "type": "password"
    }

    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(widget=forms.TextInput(attrs=attrs), label='Password', max_length=100)

class RegisterForm(forms.Form):
    attrs = {
        "type": "password"
    }

    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(widget=forms.TextInput(attrs=attrs),label='Password', max_length=100)
    first_name = forms.CharField(label='First name', max_length=35)
    last_name = forms.CharField(label='Last name', max_length=35)
    email = forms.CharField(label='Email', max_length=70)

class RegistRestaurantForm(forms.Form):
    name = forms.CharField(label='Name', max_length=70)
    city = forms.CharField(label='City', max_length=50)
    address = forms.CharField(label='Address', max_length=250)
    cuisine = forms.CharField(label='Cuisine', max_length=100)

class UserInfoForm(forms.Form):
    attrs = {
        "type": "password"
    }

    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(widget=forms.TextInput(attrs=attrs), label='Password', max_length=100)
    first_name = forms.CharField(label='First name', max_length=35)
    last_name = forms.CharField(label='Last name', max_length=35)
    email = forms.CharField(label='Email', max_length=70)