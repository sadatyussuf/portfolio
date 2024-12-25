from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status

# from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

from apps.manager import models

from .. import serializers as sm
from ..response_handle.success import Response

User = get_user_model()


# class ProjectListView(generics.ListAPIView):
#     # permission_classes = [AllowAny]
#     queryset = models.Project.objects.all()
#     serializer_class = sm.ProjectSerializer
#     permission_classes = [AllowAny]

#     @swagger_auto_schema(
#         operation_summary="List All Projects",
#         operation_description="Allows users to retrieve all available Listing.  ",
#         responses={200: "Projects retrieved successfully", 404: "Data Not Found"},
#         tags=["Projects"],
#     )
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)


# class ProjectDetailView(generics.RetrieveAPIView):
#     queryset = models.Project.objects.all()
#     serializer_class = sm.ProjectSerializer
#     permission_classes = [AllowAny]
#     lookup_field = "uid"

#     @swagger_auto_schema(
#         operation_summary="Retrieve Project by UID",
#         operation_description="Allows users to retrieve details of a Project by UID.  ",
#         responses={200: "Project retrieved successfully", 404: "Data Not Found"},
#         tags=["Projects"],
#     )
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
