import uuid
from django.db import models
from apps.skills.models import Skill, Technology  # reuse from skills app

# --------------------
# Profile
# --------------------
class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    bio = models.TextField(blank=True)
    short_intro = models.TextField(blank=True)
    resume_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Many-to-Many with Skill (flexible reuse)
    skills = models.ManyToManyField(Skill, related_name="profiles", blank=True)

    def __str__(self):
        return self.full_name


# --------------------
# Project
# --------------------
class ProjectStatus(models.TextChoices):
    PRODUCTION = "production", "Production"
    IN_PROGRESS = "in_progress", "In Progress"
    ARCHIVED = "archived", "Archived"

class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    architecture_highlight = models.TextField(blank=True)
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    api_doc_url = models.URLField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=ProjectStatus.choices,
        default=ProjectStatus.IN_PROGRESS
    )
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Many-to-Many with Technology (flexible reuse)
    technologies = models.ManyToManyField(Technology, related_name="projects", blank=True)

    def __str__(self):
        return self.title


# --------------------
# ContactMessage
# --------------------
class ContactMessage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    is_resolved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject} from {self.name}"
# --------------------
# Education
# --------------------
class Education(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    institution = models.CharField(max_length=255)
    degree = models.CharField(max_length=255, blank=True)
    field_of_study = models.CharField(max_length=255, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    profile = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name="education")

    def __str__(self):
        return f"{self.degree} at {self.institution}"


# --------------------
# Experience
# --------------------
class Experience(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    profile = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name="experiences")

    def __str__(self):
        return f"{self.role} at {self.company}"
