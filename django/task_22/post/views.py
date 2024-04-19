from django.http import HttpResponse
from django.shortcuts import render
from .models import Post, Categories

from django.views.generic import ListView
from django.db.models import Q

from django.shortcuts import get_object_or_404

from django.core.paginator import Paginator
from django.views.decorators.cache import cache_page




# Главная страница
@cache_page(30)    # Кеш на уровне представлений (30 секунд)
def post(request):
    posts = Post.objects.all().order_by('-time_created')    # сортировка в обратном порядке
    data = {
        'posts': posts,
    }
    return render(request, 'post/posts.html', context=data)

# Вывод статей по id в url http://.../post/id/
@cache_page(60)    # Кеш на уровне представлений (30 секунд)
def ful_post(request, post_id):
    posts = Post.objects.get(id=post_id)
    
    data = {
        'title': posts.title,
        'author': posts.author,
        'genre': posts.genre,
        'description': posts.description,
        'time_created': posts.time_created,
        'image': posts.image.url,
    }
    return render(request, 'post/post_id.html', context=data)

class SearchResultsView(ListView):
    ''' поиск для фронта '''
    model = Post
    template_name = 'post/search_results.html'

    def get_queryset(self): # новый
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(Q(title__icontains=query) | Q(author__name__icontains=query))
        return object_list

  
class CathResultsView(ListView):
    ''' вывод постов по категориям через поиск '''
    model = Post
    template_name = 'post/search_results.html'

    def get_queryset(self):
        # Получаем категорию по ее id или возвращаем 404, если такой категории не существует
        category = get_object_or_404(Categories, id=self.kwargs['category_id'])
        
        # Фильтруем посты по выбранной категории и возвращаем результат
        return Post.objects.filter(categories=category, is_published=True)
    
