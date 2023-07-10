from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Posts
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly


# Create your views here.
class PostListApiView(ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)  # new
    queryset = Posts.objects.all()
    serializer_class = PostSerializer


class PostDetailApiView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)  # new
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
