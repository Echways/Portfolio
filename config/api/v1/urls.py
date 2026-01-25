from django.urls import path

from config.api.views import (
    achievements_api_list,
    news_api_detail,
    news_api_list,
    projects_api_detail,
    projects_api_list,
    team_api_list,
)

urlpatterns = [
    path("news/", news_api_list, name="news-list"),
    path("news/<slug:slug>/", news_api_detail, name="news-detail"),
    path("projects/", projects_api_list, name="projects-list"),
    path("projects/<slug:slug>/", projects_api_detail, name="projects-detail"),
    path("team/", team_api_list, name="team-list"),
    path("achievements/", achievements_api_list, name="achievements-list"),
]
