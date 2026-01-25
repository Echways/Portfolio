from django.urls import path

from info.news.views import NewsDetailView, NewsListView
from info.pages.views import InfoPageView
from info.projects.views import ProjectDetailView, ProjectListView

app_name = "info"

urlpatterns = [
    path("", InfoPageView.as_view(), name="info"),
    path("news/", NewsListView.as_view(), name="news"),
    path("projects/", ProjectListView.as_view(), name="projects"),
    path("news/<slug:slug>/", NewsDetailView.as_view(), name="news-detail"),
    path("projects/<slug:slug>/", ProjectDetailView.as_view(), name="project-detail"),
]
