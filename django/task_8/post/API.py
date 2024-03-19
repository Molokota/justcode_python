# from rest_framework.permissions import AllowAny
# from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer

from rest_framework import generics



class PostAPIList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostAPICrud(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


