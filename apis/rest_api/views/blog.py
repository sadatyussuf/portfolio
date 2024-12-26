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


# class EmployeeListView(generics.ListAPIView):
#     permission_classes = [AllowAny]
#     queryset = models.Employee.objects.all()
#     serializer_class = sm.EmployeeSerializer

#     @swagger_auto_schema(
#         operation_summary="List All Employees",
#         operation_description="Allows users to retrieve all available Listing.  ",
#         responses={200: "Employees retrieved successfully", 404: "Data Not Found"},
#         tags=["Employees"],
#     )
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)


# class EmployeeDetailView(generics.RetrieveAPIView):
#     queryset = models.Employee.objects.all()
#     serializer_class = sm.EmployeeSerializer
#     permission_classes = [AllowAny]
#     lookup_field = "uid"

#     @swagger_auto_schema(
#         operation_summary="Retrieve Employee by UID",
#         operation_description="Allows users to retrieve details of a Employee by UID.  ",
#         responses={200: "Employee retrieved successfully", 404: "Data Not Found"},
#         tags=["Employees"],
#     )
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
