from pydoc import describe
from uuid import uuid4

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from django.dispatch import receiver
from django.utils import timezone
from django.utils.text import slugify
from django_quill.fields import QuillField

from .custom_manager import UserManager


class User(AbstractUser):
    email = models.EmailField(unique=True, primary_key=True)
    username = models.CharField(max_length=150, unique=False, null=False, blank=False)
    profile_pic = models.FileField()
    resume = models.FileField()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    objects = UserManager()  # type: ignore

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.email


class CommonFields(models.Model):
    """
    Description: This models is an abstract class that defines the columns that should be present in every table.
    """

    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    # created_by = models.ForeignKey(User, models.CASCADE, null=True, blank=True)

    class Meta:
        abstract = True


class Tag(CommonFields):
    # blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=155)

    def __str__(self) -> str:
        return self.name


class Project(CommonFields):
    CATEGORY_CHOICES = [("personal", "Personal"), ("professional", "Professional")]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200)
    # description = models.CharField(max_length=255)
    description = QuillField()

    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    github_link = models.CharField(max_length=250, null=True, blank=True)
    demo_link = models.CharField(max_length=250, null=True, blank=True)

    category = models.CharField(max_length=250, choices=CATEGORY_CHOICES)
    tags = models.ManyToManyField(Tag, related_name="projects")

    cover_image = models.FileField(null=True, blank=True)
    thumbnail = models.FileField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  # Automatically create a slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ToolUsed(CommonFields):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="project_tools"
    )
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Blog(CommonFields):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=200)
    # content = models.CharField(max_length=255)
    content = QuillField()
    tags = models.ManyToManyField(Tag, related_name="blog_posts")

    # image = models.FileField()
    cover_image = models.FileField()
    thumbnail = models.FileField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Skill(CommonFields):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="skills")

    LEVEL_CHOICES = [
        ("beginner", "Beginner"),
        ("intermediate", "Intermediate"),
        ("expert", "Expert"),
    ]
    name = models.CharField(max_length=255)
    level = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Testimonial(CommonFields):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="testimonials"
    )
    name = models.CharField(max_length=255)
    # content = models.CharField(max_length=255)
    content = QuillField()
    profile_pic = models.FileField()

    def __str__(self) -> str:
        return self.name
