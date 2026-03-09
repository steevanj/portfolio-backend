from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ProfileViewSet,
    ProjectViewSet,
    EducationViewSet,
    ExperienceViewSet,
    ContactMessageViewSet,
)

router = DefaultRouter()
router.register("profiles", ProfileViewSet, basename="profile")
router.register("projects", ProjectViewSet, basename="project")
router.register("education", EducationViewSet, basename="education")
router.register("experiences", ExperienceViewSet, basename="experience")
router.register("contactmessages", ContactMessageViewSet, basename="contactmessage")

urlpatterns = [
    path("", include(router.urls)),
]
