# from rest_framework.permissions import AllowAny
# from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import LargeResultsSetPagination



class PostAPIList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # фильтрация
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'genre']
    # пагинация
    pagination_class = LargeResultsSetPagination



class PostAPICrud(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


