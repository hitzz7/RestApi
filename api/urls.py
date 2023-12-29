from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ApiViewSet,CommentViewSet,AlbumViewSet,PhotoViewSet,TodosViewSet,UserViewSet

router = DefaultRouter()
router.register(r'posts', ApiViewSet, basename='api')
router.register(r'comments', CommentViewSet, basename='api')
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='api-comments')
router.register(r'albums/(?P<album_id>\d+)/photos', PhotoViewSet, basename='api-photos')
router.register(r'users/(?P<user_id>\d+)/albums', AlbumViewSet, basename='api-photos')
router.register(r'users/(?P<user_id>\d+)/todos', TodosViewSet, basename='api-photos')
router.register(r'users/(?P<user_id>\d+)/posts', ApiViewSet, basename='api-photos')
router.register(r'albums', AlbumViewSet, basename='api')
router.register(r'photos', PhotoViewSet, basename='api')
router.register(r'todos', TodosViewSet, basename='api')
router.register(r'users', UserViewSet, basename='api')


urlpatterns = router.urls