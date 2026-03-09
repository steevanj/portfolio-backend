from django.contrib import admin
from .models import Profile, Project, Education, Experience, ContactMessage

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("full_name", "title", "created_at", "updated_at")
    search_fields = ("full_name", "title")

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "featured", "created_at")
    list_filter = ("status", "featured")
    search_fields = ("title", "slug")

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("institution", "degree", "start_date", "end_date", "profile")

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("company", "role", "start_date", "end_date", "profile")

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("subject", "name", "email", "is_resolved", "created_at")
    list_filter = ("is_resolved",)
    search_fields = ("subject", "name", "email")
