from django.http import HttpResponseRedirect
from .forms import LoginUserForm
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.urls import reverse


class LoginViewController(LoginView):
    form_class = LoginUserForm
    template_name = 'accounts/login.html'


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

