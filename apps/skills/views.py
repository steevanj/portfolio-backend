from rest_framework import viewsets
from .models import Skill, Technology
from .serializers import SkillSerializer, TechnologySerializer

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all().order_by("name")
    serializer_class = SkillSerializer

class TechnologyViewSet(viewsets.ModelViewSet):
    queryset = Technology.objects.all().order_by("name")
    serializer_class = TechnologySerializer
