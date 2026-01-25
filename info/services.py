from django.utils import timezone

from info.models import News, Project


def touch_news(news: News) -> News:
    news.updated_at = timezone.now()
    news.save()
    return news


def touch_project(project: Project) -> Project:
    project.updated_at = timezone.now()
    project.save()
    return project
