from django.urls import include, path

from config.api.views import api_docs, api_root, api_schema

app_name = "api"

urlpatterns = [
    path("", api_root, name="root"),
    path("schema/", api_schema, name="schema"),
    path("docs/", api_docs, name="docs"),
    path("v1/", include("config.api.v1.urls")),
]
