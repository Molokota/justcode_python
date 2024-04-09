from typing import Any
from django import forms
# from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import User
from django.contrib.auth import get_user_model

class LoginUserForm(forms.Form):
    username = forms.CharField(label="Логин", widget=forms.TextInput())
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput())

class RegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput())
    email = forms.CharField(label='Email')
    class Meta:
        model = get_user_model()
        fields = ['username', 'password', 'password2', 'email', 'first_name', 'last_name',]
    
    def clean_email(self):
        data = self.cleaned_data
        if get_user_model().objects.filter(email=data['email']).exists():
            raise forms.ValidationError('Такой email уже зарегистрирован')
        return data['email']

    def clean_password2(self):
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError('Пароли не совпадают!')
        return data['password']