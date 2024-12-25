from pydoc import describe
from uuid import uuid4

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from django.dispatch import receiver
from django.utils import timezone
from django.utils.text import slugify

from .custom_manager import UserManager

# from django.contrib.gis.db.models import  MultiPolygonField,GeometryField


class User(AbstractUser):
    # uid = models.CharField(max_length=50, unique=True, null=True, blank=True)

    email = models.EmailField(unique=True, primary_key=True)
    username = models.CharField(max_length=150, unique=False, null=False, blank=False)

    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    objects = UserManager()  # type: ignore

    def save(self, *args, **kwargs):
        if self.is_superuser:
            self.is_admin = True
        super(User, self).save(*args, **kwargs)

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
    created_by = models.ForeignKey(User, models.CASCADE, null=True, blank=True)

    class Meta:
        abstract = True


# class Employee(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     profile_pic = models.FileField(null=True, blank=True)
#     role = models.CharField(max_length=150, null=True, blank=True)

#     phone_number = models.CharField(max_length=20, blank=True, null=True)
#     address = models.CharField(max_length=255, blank=True, null=True)
#     date_employed = models.DateField(blank=True, null=True)
#     salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
#     status = models.CharField(
#         max_length=50,
#         default="current",
#         choices=[
#             ("probation", "Probation"),
#             ("current", "Current"),
#             ("former", "Former"),
#         ],
#     )

#     created_at = models.DateTimeField(db_index=True, default=timezone.now)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"{self.user.username} - {self.role}"


class Project(CommonFields):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    content = models.TextField(blank=True)

    customer = models.CharField(max_length=150, null=True, blank=True)

    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    location = models.CharField(max_length=255)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)

    total_cost = models.DecimalField(max_digits=15, decimal_places=2)
    invoice_amount = models.DecimalField(max_digits=15, decimal_places=2)
    status = models.CharField(
        max_length=50, choices=[("published", "Published"), ("draft", "Draft")]
    )

    def __str__(self):
        return self.title


class ProjectImage(CommonFields):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="project_images"
    )

    title = models.CharField(max_length=255)
    image = models.FileField()
    is_cover_image = models.BooleanField(default=False)
    is_thumbnail = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title


class ProjectFile(CommonFields):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="project_files"
    )

    title = models.CharField(max_length=255)
    file = models.FileField()

    def __str__(self) -> str:
        return self.title


# class ProjectParticipant(CommonFields):
#     ROLE_CHOICES = [("field_worker", "Field Worker"), ("manager", "Manager")]

#     project = models.ForeignKey(
#         Project, on_delete=models.CASCADE, related_name="project_participants"
#     )
#     employee = models.ForeignKey(
#         User, on_delete=models.CASCADE, related_name="projects"
#     )
#     role = models.CharField(max_length=250, choices=ROLE_CHOICES)
#     bonus = models.DecimalField(max_digits=10, decimal_places=2)

#     class Meta:  # type: ignore
#         unique_together = ("project", "employee", "role")

#     def __str__(self):
#         return f"{self.employee.username} - {self.role} in {self.project.title}"


# class OperationalCost(CommonFields):
#     project = models.ForeignKey(
#         Project, on_delete=models.CASCADE, related_name="operational_costs"
#     )
#     description = models.CharField(max_length=255)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     date_incurred = models.DateField()

#     def __str__(self):
#         return f"{self.description} - {self.amount} for {self.project.title}"
