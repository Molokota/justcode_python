from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('my/', views.my, name='my'),
    path('registration/', views.registration, name='registration'),

    # api account detail
    path('<int:pk>', views.AccountDetailApi.as_view(), name='account'),
]


