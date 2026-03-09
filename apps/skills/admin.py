from django.contrib import admin
from .models import Skill, Technology

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "icon")
    list_filter = ("category",)
    search_fields = ("name",)

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ("name", "icon")
    search_fields = ("name",)
