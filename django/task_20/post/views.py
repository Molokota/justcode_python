from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

from django.views.generic import ListView
from django.db.models import Q




# Главная страница
def post(request):
    posts = Post.objects.all()
    data = {
        'posts': posts,
    }
    return render(request, 'post/posts.html', context=data)

# Вывод статей по id в url http://.../post/id/
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


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def template_test(request):
    return render(request, 'template_test.html')

class SearchResultsView(ListView):
    ''' поиск для фронта '''
    model = Post
    template_name = 'post/search_results.html'

    def get_queryset(self): # новый
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(Q(title__icontains=query) | Q(author__name__icontains=query))
        return object_list

