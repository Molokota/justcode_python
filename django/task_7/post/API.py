from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer


from rest_framework import mixins
from rest_framework import generics

class PostApi(mixins.RetrieveModelMixin,
              mixins.UpdateModelMixin,
              mixins.DestroyModelMixin,
              generics.GenericAPIView):

    permission_classes = [AllowAny]

    queryset = Post.objects.all()
    serializer_class = PostSerializer


    def delete(self, request, *args, **kwargs):
        result_delete = self.destroy(request, *args, **kwargs)
        return Response({'post': 'пост удален'})