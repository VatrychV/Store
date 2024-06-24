from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import buy_and_ship,Contact

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2','is_staff']
        labels = {'username': 'Username', 'email': 'Email'}
        help_texts = {'username': 'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
                      'email': 'Required. Example: XXXXXXXXXXXXXXXX'}
        error_messages = {'username': {'max_length': '150 characters or fewer.'},
                          'email': {'required': 'Email is required.'}}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'}),
                   'email': forms.TextInput(attrs={'class': 'form-control'})} 
        """
                   'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
                   'password2': forms.PasswordInput(attrs={'class': 'form-control'})}"""
        
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'number', 'message']

class buy_and_shipForm(forms.ModelForm):
    class Meta:
        model = buy_and_ship
        fields = ['first_name', 'last_name', 'address', 'email', 'phone', 'additional_information', 'price']