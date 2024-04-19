from typing import Any
from django import forms
from django.contrib.auth.forms import User
from django.contrib.auth import get_user_model
from requests import get

class LoginUserForm(forms.Form):
    username = forms.CharField(label="Email", widget=forms.TextInput())
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput())

class RegistrationForm(forms.ModelForm):
    nickname = forms.CharField(label='Nickname',max_length=30, required=False)
    # username = forms.CharField(label='Логин'),
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput())
    email = forms.CharField(label='Email')
    mobile_phone =  forms.CharField(label='Мобильный тел.', max_length=12, required=False,)
    
    
    class Meta:
        model = get_user_model()
        fields = ['nickname', 'password', 'password2', 'email', 'first_name', 'last_name',]
    
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

# https://www.ipify.org/ ipify API получение ip пользователя
def get_user_ip(request):
    ip = get('https://api.ipify.org').text
    ip_address = '{}'.format(ip)
    return ip_address

class ImageUploadForm(forms.Form):
    ''' загрузка изобржения пользователя в личный кабинет'''
    image = forms.ImageField(label='Чтобы сменить изображение')