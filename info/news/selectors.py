from django.shortcuts import get_object_or_404

from info.models import News


def news_list():
    return News.objects.all()


def news_by_slug(slug: str):
    return get_object_or_404(News, slug=slug)
