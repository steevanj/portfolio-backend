from rest_framework import serializers
from .models import Profile, Project, Education, Experience, ContactMessage
from apps.skills.models import Skill, Technology

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ["id", "name", "category", "icon"]

class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ["id", "name", "icon"]

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = "__all__"

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = "__all__"

class ProfileSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)
    education = EducationSerializer(many=True, read_only=True)
    experiences = ExperienceSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = "__all__"

class ProjectSerializer(serializers.ModelSerializer):
    technologies = TechnologySerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = "__all__"

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = "__all__"
