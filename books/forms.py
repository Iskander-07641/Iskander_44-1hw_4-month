from django import forms
from .models import Book
from django.contrib.auth.models import User


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)