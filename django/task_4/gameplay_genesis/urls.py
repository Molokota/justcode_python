from django.contrib import admin
from django.urls import path, include
from book.views import page_404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('book.urls')),
    # пути до файла урл других приложений ...
]

handler404 = page_404
