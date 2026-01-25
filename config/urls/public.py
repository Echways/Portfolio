from django.urls import include, path


urlpatterns = [
    path("", include(("config.core.urls", "core"), namespace="core")),
    path("api/", include(("config.api.urls", "api"), namespace="api")),
    path("", include(("info.urls", "info"), namespace="info")),
]
