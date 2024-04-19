from django.urls import path
from . import views
from django.conf import settings 
from django.conf.urls.static import static
from .API import  PostAPIList, PostAPICrud

urlpatterns = [
    path('', views.post, name='home'),
    path('post/<int:post_id>/', views.ful_post),
    path('api/book/', PostAPIList.as_view()),
    path('api/book/<int:pk>/', PostAPICrud.as_view()),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),    # поиск для фронта
    path('category/<int:category_id>/', views.CathResultsView.as_view(), name='category_results'),   # по категориям для меню
]



if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

