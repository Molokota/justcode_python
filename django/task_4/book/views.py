from django.http import HttpResponse, HttpResponseNotFound, Http404

# Create your views here.
def posts(request):
    return HttpResponse('<h1>Мой первый пост</h1>')


def page_404(request, exception):
    return HttpResponseNotFound("Not Found 404")




