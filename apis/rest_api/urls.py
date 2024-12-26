# myapp/urls.py
from django.urls import path

from .views import auth, blog, project

urlpatterns = [
    path("auth/register", auth.SignUpView.as_view(), name="register"),
    path("auth/login", auth.LoginView.as_view(), name="login"),
    # path("auth/password_reset", auth.PasswordReset.as_view(), name="password-reset"),
    # # path("users/", admin.UserListView.as_view(), name="user-list"),
    # path("admins/me/", admin.AdminDetailView.as_view(), name="user-detail"),
    # path("admins/me/delete/", admin.AdminDeleteView.as_view(), name="user-delete"),
    # path("employees", employee.EmployeeListView.as_view(), name="employee-list"),
    # path(
    #     "employees/<str:id>",
    #     employee.EmployeeDetailView.as_view(),
    #     name="employee-detail",
    # ),
    # path("projects", project.ProjectListView.as_view(), name="project-list"),
    # path(
    #     "projects/<str:id>",
    #     project.ProjectDetailView.as_view(),
    #     name="project-detail",
    # ),
]
