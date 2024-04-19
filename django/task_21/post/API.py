
from .models import Post
from .serializers import PostSerializer
from rest_framework import generics
from .pagination import LargeResultsSetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework import response

#filter
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend



class PostAPIList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # Authorization
    permission_classes = (IsAuthenticated,)
    # фильтрация
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'genre', 'is_published',]    # фильтрация по полю
    search_fields = ['description']    # фильтрация по тексту в данном поле
    ordering_fields = '__all__'   # сортировка по любому полю в модели
    # пагинация
    pagination_class = LargeResultsSetPagination
   

class PostAPICrud(generics.RetrieveUpdateDestroyAPIView):
    ''' get, post, put, delete запрос к посту '''
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,) # проверка авторизации jwt

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        message = "Пост был удален!"
        return response.Response({"message": message})
    
    def put(self, request, *args, **kwargs):
        super().put(request, *args, **kwargs)
        message = "Пост был отредактирован!"
        return response.Response({"message": message})
    