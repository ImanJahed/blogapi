from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register('users', views.UserViewSet, basename='users')
router.register('', views.PostViewSet, basename='posts')

urlpatterns = router.urls

# urlpatterns = [
#     path('', views.PostListApiView.as_view(), name='post-list-api'),
#     path('<int:pk>', views.PostDetailApiView.as_view(), name='post-detail-api'),
#     path('users', views.UserListApiView.as_view(), name='user-list-api'),
#     path('users/<int:pk>', views.UserDetailApiView.as_view(), name='user-detail-api'),
# ]