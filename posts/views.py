from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Posts
from .serializers import PostsSerializer
from .permissions import IsAuthorOrReadOnly

# Create your views here.
class PostListApiView(ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    permission_classes = IsAuthorOrReadOnly,


class PostDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    permission_classes = IsAuthorOrReadOnly,
    serializer_class = PostsSerializer
