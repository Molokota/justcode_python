from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import LoginUserForm, RegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

#api
from rest_framework import generics
from rest_framework.response import Response
from .serializers import RegisterSerializer, UserSerializer
from .models import User
from rest_framework import response

from .ip_user import get_user_ip


class RegisterApi(generics.GenericAPIView):
    ''' регистраци аккаунта через api '''
    serializer_class = RegisterSerializer
    
    # запрос регистрации через api
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user,    context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })
    
    # запрос получения списка всех пользователей через api
    def get(self, request, *args,  **kwargs):
        users = User.objects.all()
        user_data = UserSerializer(users, many=True)
        return response.Response(user_data.data)

class AccountDetailApi(generics.RetrieveUpdateDestroyAPIView):
    ''' запрос получения данных пользователея по id через api (get, put, delete)'''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    # вывод сообщения после удаление аккаунта
    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        message = "Aккаунт был удален!"
        return response.Response({"message": message})
    
    # вывод сообщения после редактирования данных аккаунта
    def put(self, request, *args, **kwargs):
        super().put(request, *args, **kwargs)
        message = "Аккаунт был отредактирован!"
        return response.Response({"message": message})


def login_user(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
    else:
        form = LoginUserForm()
    return render(request, 'accounts/login.html', {'form':form})

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = form.save(commit=False)
            user.set_password(data['password'])
            user.save()
            return redirect('/accounts/login/')  
    else:
        form = RegistrationForm()
    return render(request, 'accounts/registration.html', context={'form': form})


@login_required    # Декоратор проверки аутентификации
def my(request):
    # получение ip адреса пользователя  ipify API
    ip_address = get_user_ip(request)


    return render(request, 'accounts/my.html', {'ip_address': ip_address})




