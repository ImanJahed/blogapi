from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostListApiView.as_view(), name='post-list-api'),
    path('<int:pk>', views.PostDetailApiView.as_view(), name='post-detail-api'),
]