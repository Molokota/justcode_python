from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    print('request')
    print(request.scheme)
    print(request.path)
    print(request.encoding)
    return HttpResponse("<h1>Hello world</h1>")

def about(request):
    print(request.get_full_path)
    return HttpResponse('<a href="#"> about pach!</a>')

def ggg(request):
    return HttpResponse('<h2>G-g-g</h2>')

def contacts(request):
    return HttpResponse('<h2>contacts page</h2>')

def number(request):
    return HttpResponse('<h2>NUMBER</h2>')

def sgroup(request):
    return HttpResponse('<h1>group</h1>')

def home(request):
    return render(request, 'home.html')



