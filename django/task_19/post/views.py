from django.http import HttpResponse
from django.shortcuts import render
from .models import Post


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

