from django.urls import path, re_path

from . import views 

urlpatterns = [
    path('index/', views.index),
    re_path(r'^about/$', views.about),    # начало и конец
    re_path(r'^g+', views.ggg),    # потор 1 или более раз
    re_path(r'^contact(?:s)?/$', views.contacts),    # повтор либо 0 или 1 раз
    re_path(r'^number/\d{3}/$', views.number),    # ограничение кол-ва цифр
    re_path(r'^archive-2/19\d{2}/$', views.number),    # вход символов
    re_path(r'^archive-2/1[7-9]\d{2}/$', views.number),    # вход символов
    re_path(r'^sgroup/[A-C]\d{4}/$', views.sgroup),    # вхождкение букв алфавита

]
