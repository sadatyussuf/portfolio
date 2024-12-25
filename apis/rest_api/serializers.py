from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers, status

from apps.manager import models

User = get_user_model()


class RegisterUserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=50)

    class Meta:
        model = User
        fields = [
            "email",
            "username",
            "password",
            "confirm_password",
        ]

        extra_kwargs = {"password": {"write_only": True}, "uid": {"read_only": True}}

    def validate_password(self, value):
        validate_password(value)
        return value

    def validate(self, attrs):
        password = attrs.get("password")
        confirm_password = attrs.pop("confirm_password", None)

        if password and confirm_password and password != confirm_password:
            raise serializers.ValidationError(
                "Password and confirm password do not match."
            )

        return attrs

    def create(self, validated_data):
        user = super(RegisterUserSerializer, self).create(validated_data)
        user.set_password(validated_data["password"])
        user.save()

        return user


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()
    new_password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(max_length=50)

    class Meta:
        # model = User
        fields = [
            "email",
            "new_password",
            "confirm_password",
        ]

    def validate(self, attrs):
        email = attrs.get("email")

        find_email = User.objects.filter(email=email).exists()
        if not find_email:
            raise serializers.ValidationError(
                "Email Not Found", code=status.HTTP_404_NOT_FOUND
            )

        password = attrs.get("new_password")
        confirm_password = attrs.pop("confirm_password", None)
        if password and confirm_password and password != confirm_password:
            raise serializers.ValidationError(
                "Password and confirm password do not match."
            )

        return attrs


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "email",
            "password",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        if email and password:
            user = authenticate(email=email, password=password)

            if not user:
                raise serializers.ValidationError(
                    "Unable to log in with provided credentials."
                )
        else:
            raise serializers.ValidationError(
                "Both email and password are required for login."
            )

        attrs["user"] = user
        return attrs


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "username", "is_admin"]


# class EmployeeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Employee
#         fields = [
#             "user",
#             "profile_pic",
#             "role",
#             "phone_number",
#             "address",
#             "date_employed",
#             "salary",
#             "status",
#             "created_at",
#             "updated_at",
#         ]


# class ProjectImageSerilizer(serializers.ModelSerializer):
#     class Meta:
#         model = models.ProjectImage
#         fields = ["title", "image", "is_cover_image", "is_thumbnail"]


# class ProjectFileSerilizer(serializers.ModelSerializer):
#     class Meta:
#         model = models.ProjectFile
#         fields = [
#             "title",
#             "file",
#         ]


# class ProjectParticipantSerilizer(serializers.ModelSerializer):
#     class Meta:
#         model = models.ProjectParticipant
#         fields = ["role", "bonus"]


# class OperationalCostSerilizer(serializers.ModelSerializer):
#     class Meta:
#         model = models.OperationalCost
#         fields = ["description", "amount", "date_incurred"]


# class ProjectSerializer(serializers.ModelSerializer):

#     project_images = ProjectImageSerilizer(many=True)
#     project_files = ProjectFileSerilizer(many=True)

#     project_participants = ProjectParticipantSerilizer(many=True)
#     operational_costs = OperationalCostSerilizer(many=True)

#     class Meta:
#         model = models.Project
#         fields = "__all__"
