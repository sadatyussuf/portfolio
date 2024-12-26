from typing import Any

from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import Group
from django.db import models
from django.db.models.query import QuerySet
from django.http import HttpRequest
from django.shortcuts import redirect
from django.urls import reverse
from unfold.admin import ModelAdmin, StackedInline, TabularInline
from unfold.contrib.filters.admin import (
    ChoicesDropdownFilter,
    DropdownFilter,
    MultipleChoicesDropdownFilter,
    MultipleDropdownFilter,
    MultipleRelatedDropdownFilter,
    RelatedDropdownFilter,
)
from unfold.contrib.forms.widgets import WysiwygWidget
from unfold.decorators import display

from .models import Blog, Project, Skill, Tag, Testimonial, ToolUsed, User

admin.site.unregister(Group)


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass


class SkillInline(TabularInline):
    model = Skill
    extra = 1
    fields = ("user", "name", "level")
    autocomplete_fields = ["user"]


class ToolUsedInline(TabularInline):
    model = ToolUsed
    extra = 1
    fields = ("name",)


@admin.register(User)
class UserAdmin(ModelAdmin):

    list_display = (
        "email",
        "username",
    )
    search_fields = ["username", "email"]

    fieldsets = (
        ("Personal Info", {"fields": ("email", "username", "resume", "profile_pic")}),
        (
            "Permissions",
            {
                "classes": ["collapse"],
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )

    ordering = ("email",)

    inlines = [SkillInline]


@admin.register(Project)
class ProjectAdmin(ModelAdmin):
    list_filter_submit = True

    list_display = (
        "title",
        "start_date",
        "end_date",
        "category",
    )
    list_filter = ("category", "start_date", "end_date")
    search_fields = ("category", "title", "start_date", "end_date")

    inlines = [ToolUsedInline]

    fieldsets = (
        (
            "Project Details",
            {
                "fields": (
                    "title",
                    "description",
                    "slug",
                    ("github_link", "demo_link"),
                )
            },
        ),
        (
            "Dates & Status",
            {"classes": ("tab"), "fields": (("start_date", "end_date", "category"),)},
        ),
        ("Images", {"fields": (("cover_image", "thumbnail"),)}),
        ("Tags", {"fields": ("tags",)}),
    )


@admin.register(Blog)
class BlogAdmin(ModelAdmin):
    list_filter_submit = True

    list_display = (
        "title",
        "created_at",
        "updated_at",
    )
    list_filter = ("created_at", "updated_at")
    search_fields = ("title",)

    fieldsets = (
        (
            "Blog Details",
            {
                "fields": (
                    "title",
                    "content",
                    "slug",
                )
            },
        ),
        (
            "Dates",
            {"classes": ("tab"), "fields": (("created_at",),)},
        ),
        ("Images", {"fields": (("cover_image", "thumbnail"),)}),
        ("Tags", {"fields": ("tags",)}),
    )


@admin.register(Testimonial)
class TestimonialAdmin(ModelAdmin):
    list_display = ("name",)
    search_fields = ("user",)
