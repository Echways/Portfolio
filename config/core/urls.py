from django.urls import path

from config.core.views import healthcheck_view

app_name = "core"

urlpatterns = [
    path("health/", healthcheck_view, name="health"),
]
