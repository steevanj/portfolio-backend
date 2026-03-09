from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogPostViewSet, BlogTagViewSet

router = DefaultRouter()
router.register("posts", BlogPostViewSet, basename="blogpost")
router.register("tags", BlogTagViewSet, basename="blogtag")

urlpatterns = [
    path("", include(router.urls)),
]
