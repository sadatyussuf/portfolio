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

from .models import (  # OperationalCost,; Project,; ProjectFile,; ProjectImage,; ProjectParticipant,; Employee,
    User,
)

admin.site.unregister(Group)


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass


# class EmployeeInline(StackedInline):
#     model = Employee
#     extra = 1
#     fields = (
#         "profile_pic",
#         "role",
#         "phone_number",
#         "address",
#         "date_employed",
#         "salary",
#         "status",
#     )


# class ProjectParticipantInline(TabularInline):
#     model = ProjectParticipant
#     extra = 1
#     fields = ("employee", "role", "bonus")
#     autocomplete_fields = ["employee"]


# class OperationalCostInline(TabularInline):
#     model = OperationalCost
#     extra = 1
#     fields = ("description", "amount", "date_incurred")


# class ProjectFileInline(TabularInline):
#     model = ProjectFile
#     extra = 1
#     fields = ("title", "file")


# class ProjectImageInline(TabularInline):
#     model = ProjectImage
#     extra = 1
#     fields = ("title", "image", "is_cover_image", "is_thumbnail")


# @admin.register(User)
# class UserAdmin(ModelAdmin):

#     def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
#         return super(UserAdmin, self).get_queryset(request).select_related("employee")

#     list_display = (
#         "email",
#         "username",
#         "status",
#         "role",
#         "address",
#         "date_employed",
#         "salary",
#         "last_login",
#         "date_joined",
#         "is_staff",
#     )
#     search_fields = ["username", "email"]

#     fieldsets = (
#         ("Personal Info", {"fields": ("email", "username", "password")}),
#         (
#             "Permissions",
#             {
#                 "classes": ["collapse"],
#                 "fields": (
#                     "is_active",
#                     "is_staff",
#                     "is_superuser",
#                     "groups",
#                     "user_permissions",
#                 ),
#             },
#         ),
#     )

#     ordering = ("email",)
#     inlines = [EmployeeInline]

#     def status(self, obj):
#         return obj.employee.status

#     def role(self, obj):
#         return obj.employee.role

#     def address(self, obj):
#         return obj.employee.address

#     def date_employed(self, obj):
#         return obj.employee.date_employed

#     def salary(self, obj):
#         return obj.employee.salary


# @admin.register(Project)
# class ProjectAdmin(ModelAdmin):
#     list_filter_submit = True

#     list_display = (
#         "title",
#         "location",
#         "customer",
#         "start_date",
#         "end_date",
#         "total_cost",
#         "status",
#     )
#     list_filter = ("status", "location", "start_date", "end_date")
#     search_fields = ("title", "description", "location", "status")

#     inlines = [
#         ProjectImageInline,
#         ProjectFileInline,
#         ProjectParticipantInline,
#         OperationalCostInline,
#     ]

#     fieldsets = (
#         (
#             "Project Details",
#             {
#                 "fields": (
#                     "title",
#                     "description",
#                     "customer",
#                     "content",
#                     ("location", "longitude", "latitude"),
#                 )
#             },
#         ),
#         (
#             "Dates & Status",
#             {"classes": ("tab"), "fields": (("start_date", "end_date", "status"),)},
#         ),
#         ("Financials", {"fields": (("total_cost", "invoice_amount"),)}),
#     )

#     formfield_overrides = {
#         models.TextField: {
#             "widget": WysiwygWidget,
#         }
#     }


# @admin.register(Employee)
# class EmployeeAdmin(ModelAdmin):
#     list_display = (
#         "user",
#         "role",
#         "phone_number",
#         "address",
#         "date_employed",
#         "salary",
#         "status",
#     )
#     list_filter = ("status",)
#     search_fields = (
#         "user__username",
#         "role",
#         "phone_number",
#         "address",
#         "date_employed",
#         "salary",
#         "status",
#     )

#     autocomplete_fields = ["user"]


# @admin.register(ProjectParticipant)
# class ProjectParticipantAdmin(ModelAdmin):
#     list_display = ("project", "employee", "role", "bonus")
#     # list_filter = ('role', 'project__status')
#     search_fields = ("project__title", "employee__user__username", "role")
#     autocomplete_fields = ["project", "employee"]


# @admin.register(OperationalCost)
# class OperationalCostAdmin(ModelAdmin):
#     list_display = ("project", "description", "amount", "date_incurred")
#     # list_filter = ('date_incurred',)
#     search_fields = ("project__title", "description")
#     autocomplete_fields = ["project"]


# @admin.register(ProjectImage)
# class ProjectImageAdmin(ModelAdmin):
#     list_display = ("project", "title", "is_cover_image", "is_thumbnail")
#     search_fields = ("project__title", "title")
#     autocomplete_fields = ["project"]


# @admin.register(ProjectFile)
# class ProjectFileAdmin(ModelAdmin):
#     list_display = ("project", "title")
#     # list_filter = ('date_incurred',)
#     search_fields = ("project__title", "title")
#     autocomplete_fields = ["project"]
