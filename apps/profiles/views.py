from rest_framework import viewsets
from .models import Profile, Project, Education, Experience, ContactMessage
from .serializers import (
    ProfileSerializer,
    ProjectSerializer,
    EducationSerializer,
    ExperienceSerializer,
    ContactMessageSerializer,
)

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all().order_by("-created_at")
    serializer_class = ContactMessageSerializer
