from django.urls import path
from . import views
from django.conf import settings 
from django.conf.urls.static import static

from .API import  PostAPIList, PostAPICrud

urlpatterns = [
    path('', views.post, name='home'),
    path('post/<int:post_id>/', views.ful_post),
    path('template_example/', views.template_test),
    path('api/book/', PostAPIList.as_view()),
    path('api/book/<int:pk>/', PostAPICrud.as_view()),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),    # поиск для фронта
]



if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

