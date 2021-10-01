from django.contrib import admin
from django.urls import path

from rest_framework.schemas import get_schema_view

from core.views import HealthView


urlpatterns = [
    path(
        "openapi",
        get_schema_view(
            title="{{cookiecutter.project_name}}", description="{{cookiecutter.project_name}}"
        ),
        name="openapi-schema",
    ),
    path("admin/", admin.site.urls),
    path("health", HealthView.as_view()),
]
