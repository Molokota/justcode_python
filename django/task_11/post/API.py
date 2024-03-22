
from .models import Post
from .serializers import PostSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import LargeResultsSetPagination
from rest_framework.permissions import IsAuthenticated





class PostAPIList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)
    # фильтрация
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'genre']
    # пагинация
    pagination_class = LargeResultsSetPagination
   

class PostAPICrud(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)



