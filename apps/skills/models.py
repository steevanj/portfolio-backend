from django.db import models
import uuid

class SkillCategory(models.TextChoices):
    BACKEND = "backend", "Backend"
    DATABASE = "database", "Database"
    DEVOPS = "devops", "DevOps"
    ARCHITECTURE = "architecture", "Architecture"   
    TOOLS = "tools", "Tools"

class Skill(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=50, choices=SkillCategory.choices)
    icon = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.name} ({self.category})"

class Technology(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    icon = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name