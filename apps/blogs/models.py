import uuid
from django.db import models

class BlogTag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    is_published = models.BooleanField(default=False)
    read_time = models.PositiveIntegerField(help_text="Estimated read time in minutes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Many-to-Many with BlogTag
    tags = models.ManyToManyField(BlogTag, related_name="posts", blank=True)

    def __str__(self):
        return self.title
