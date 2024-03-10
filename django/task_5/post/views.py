from django.http import HttpResponse
from django.shortcuts import render
from .models import Post


# Главная страница
def post(request):
    posts = Post.objects.all()
    data = {
        'title': 'All posts',
        'message': 'hello guys!',
        'posts': posts,
    }
    return render(request, 'posts.html', context=data)
    # return HttpResponse('<h1>Страница с постами</h1>')

def ful_post(request, post_id):
    posts = Post.objects.get(id=post_id)
    
    data = {
        'image': posts.image,
        'title': posts.title,
        'author': posts.author,
        'genre': posts.genre,
        'description': posts.description,
        'time_created': posts.time_created,
        'image': posts.image.url,
    }
    return render(request, 'post_id.html', context=data)


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def template_test(request):
    return render(request, 'template_test.html')
