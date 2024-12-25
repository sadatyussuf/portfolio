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


# Create your views here.
class SignUpView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = sm.RegisterUserSerializer

    @swagger_auto_schema(
        operation_summary="Signup User Account",
        operation_description="Allows users to register their account.",
        responses={201: "User Signup successfully", 404: "Data Not Found"},
        tags=["Accounts"],
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)

        refresh = RefreshToken.for_user(user=user)
        data = {
            "access_token": str(refresh.access_token),  # type: ignore
            "token_type": "bearer",
        }
        return Response(data=data)

    def perform_create(self, serializer):
        return serializer.save()


class LoginView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = sm.LoginSerializer

    @swagger_auto_schema(
        operation_summary="Login User Account",
        operation_description="Allows users to login their account.",
        responses={200: "User Login successfully", 404: "Data Not Found"},
        tags=["Accounts"],
    )
    def post(self, request, *args, **kwargs):
        serializer = sm.LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]  # type: ignore

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)  # type: ignore

        return Response(
            data={"access_token": access_token, "token_type": "bearer"},
            status=status.HTTP_200_OK,
        )


# class PasswordReset(generics.CreateAPIView):
#     permission_classes = [AllowAny]
#     serializer_class = sm.PasswordResetSerializer

#     def post(self, request, *args, **kwargs):

#         serializer = sm.PasswordResetSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         email = serializer.validated_data.get('email',None) # type: ignore
#         new_password = serializer.validated_data.get('new_password',None) # type: ignore


#         user = User.objects.filter(email=email).first()
#         if user:
#             user.set_password(new_password)
#             user.save()

#         # print(serializer.validated_data,email)


#         return Response({"message": "New Password Created"},status=status.HTTP_200_OK)
