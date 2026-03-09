from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SkillViewSet, TechnologyViewSet

router = DefaultRouter()
router.register("skills", SkillViewSet, basename="skill")
router.register("technologies", TechnologyViewSet, basename="technology")

urlpatterns = [
    path("", include(router.urls)),
]
