from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import LoginUserForm, RegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect


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
    return render(request, 'accounts/my.html')

