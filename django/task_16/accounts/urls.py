from django.urls import path
from . import views


app_name = "accounts"
urlpatterns = [
    path('login/', views.LoginViewController.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
]


