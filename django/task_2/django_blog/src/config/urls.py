from django.contrib import admin
from django.urls import path, re_path, include

from post.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', include('post.urls')),
    path('home/', home),
    # пути до файла урл других приложений ...
]
