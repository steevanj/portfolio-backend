from django.contrib import admin
from .models import BlogPost, BlogTag

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "is_published", "read_time", "created_at")
    list_filter = ("is_published",)
    search_fields = ("title", "slug")

@admin.register(BlogTag)
class BlogTagAdmin(admin.ModelAdmin):
    list_display = ("name",)
