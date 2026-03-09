from rest_framework import serializers
from .models import Skill, Technology

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ["id", "name", "category", "icon"]

class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ["id", "name", "icon"]
