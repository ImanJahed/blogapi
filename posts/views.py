from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth import get_user_model

from .models import Posts
from .serializers import PostSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly


# Create your views here.
# class PostListApiView(ListCreateAPIView):
#     permission_classes = (IsAuthorOrReadOnly,)  # new
#     queryset = Posts.objects.all()
#     serializer_class = PostSerializer
#
#
# class PostDetailApiView(RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthorOrReadOnly,)  # new
#     queryset = Posts.objects.all()
#     serializer_class = PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Posts.objects.all()
    serializer_class = PostSerializer


# class UserListApiView(ListCreateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetailApiView(RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
