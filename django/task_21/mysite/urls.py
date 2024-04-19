
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from accounts import views
urlpatterns = [
    path('', include('post.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),

    # Регистрация по JWT
    path('api/register/', views.RegisterApi.as_view(), name='register'),
    # Авторизация по JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path("__debug__/", include("debug_toolbar.urls"))
]
