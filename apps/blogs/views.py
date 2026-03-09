from rest_framework import viewsets
from .models import BlogPost, BlogTag
from .serializers import BlogPostSerializer, BlogTagSerializer

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.filter(is_published=True).order_by("-created_at")
    serializer_class = BlogPostSerializer

class BlogTagViewSet(viewsets.ModelViewSet):
    queryset = BlogTag.objects.all()
    serializer_class = BlogTagSerializer
