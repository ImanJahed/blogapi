from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Posts
from .serializers import PostsSerializer


# Create your views here.
class PostListApiView(ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer


class PostDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
