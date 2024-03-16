from django.urls import path
from . import views
from django.conf import settings 
from django.conf.urls.static import static

from .API import PostApi

urlpatterns = [
    path('', views.index, name='index'), 
    path('post/', views.post),
    path('post/<int:post_id>/', views.ful_post),
    path('template_example/', views.template_test),
    path('api/book/<int:pk>/', PostApi.as_view()),
]



if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

