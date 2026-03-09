from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django Admin
    path("me/", admin.site.urls),

    # API routes
    path("api/blogs/", include("apps.blogs.urls")),
    path("api/profiles/", include("apps.profiles.urls")),
    path("api/skills/", include("apps.skills.urls")),
]
