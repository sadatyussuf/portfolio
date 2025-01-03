from django.urls import path

from .views import homepage_view

urlpatterns = [
    path("", homepage_view, name="home-page"),
    # path("blogs", project_view, name="blog-list"),
]
