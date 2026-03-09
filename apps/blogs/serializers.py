from rest_framework import serializers
from .models import BlogPost, BlogTag

class BlogTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogTag
        fields = ["id", "name"]

class BlogPostSerializer(serializers.ModelSerializer):
    tags = BlogTagSerializer(many=True, read_only=True)

    class Meta:
        model = BlogPost
        fields = [
            "id",
            "title",
            "slug",
            "content",
            "excerpt",
            "is_published",
            "read_time",
            "created_at",
            "updated_at",
            "tags",
        ]
