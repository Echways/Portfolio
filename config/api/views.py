import math

from django.http import JsonResponse
from django.shortcuts import render

from info.achievements.selectors import achievements_list
from info.news.selectors import news_by_slug, news_list
from info.projects.selectors import project_by_slug, projects_list
from info.team.selectors import team_members_active

DEFAULT_PAGE_SIZE = 6
MAX_PAGE_SIZE = 50


def _news_payload(news):
    return {
        "title": news.title,
        "slug": news.slug,
        "description": news.description,
        "preview": news.preview_text,
        "image": news.image.url if news.image else None,
        "created_at": news.created_at.isoformat(),
        "updated_at": news.updated_at.isoformat(),
        "url": f"/news/{news.slug}/",
    }


def _project_payload(project):
    return {
        "title": project.title,
        "slug": project.slug,
        "description": project.description,
        "preview": project.preview_text,
        "image": project.image.url if project.image else None,
        "created_at": project.created_at.isoformat(),
        "updated_at": project.updated_at.isoformat(),
        "url": f"/projects/{project.slug}/",
    }


def _team_payload(member):
    return {
        "name": member.name,
        "skills": member.skills,
        "telegram_url": member.telegram_url,
        "instagram_url": member.instagram_url,
        "order": member.order,
    }


def _achievement_payload(achievement):
    return {
        "id": achievement.id,
        "text": achievement.text,
    }


def _parse_pagination(request):
    try:
        page = int(request.GET.get("page", "1"))
    except ValueError:
        page = 1
    try:
        page_size = int(request.GET.get("page_size", str(DEFAULT_PAGE_SIZE)))
    except ValueError:
        page_size = DEFAULT_PAGE_SIZE
    page = max(page, 1)
    page_size = max(1, min(page_size, MAX_PAGE_SIZE))
    return page, page_size


def _build_page_url(request, page, page_size):
    query = request.GET.copy()
    query["page"] = page
    query["page_size"] = page_size
    return request.build_absolute_uri(f"{request.path}?{query.urlencode()}")


def _paginate(request, queryset, serializer):
    page, page_size = _parse_pagination(request)
    total = queryset.count()
    num_pages = max(1, math.ceil(total / page_size)) if total else 1
    if page > num_pages:
        page = num_pages
    start = (page - 1) * page_size
    end = start + page_size
    items = list(queryset[start:end])
    results = [serializer(item) for item in items]
    next_url = _build_page_url(request, page + 1, page_size) if page < num_pages else None
    prev_url = _build_page_url(request, page - 1, page_size) if page > 1 else None
    return {
        "count": total,
        "page": page,
        "page_size": page_size,
        "num_pages": num_pages,
        "next": next_url,
        "previous": prev_url,
        "results": results,
    }


def api_root(request):
    return JsonResponse(
        {
            "status": "ok",
            "versions": ["v1"],
            "endpoints": {
                "health": "/health/",
                "schema": "/api/schema/",
                "docs": "/api/docs/",
                "news": "/api/v1/news/",
                "projects": "/api/v1/projects/",
                "team": "/api/v1/team/",
                "achievements": "/api/v1/achievements/",
            },
        }
    )


def news_api_list(request):
    payload = _paginate(request, news_list(), _news_payload)
    return JsonResponse(payload)


def news_api_detail(request, slug: str):
    news = news_by_slug(slug)
    return JsonResponse(_news_payload(news))


def projects_api_list(request):
    payload = _paginate(request, projects_list(), _project_payload)
    return JsonResponse(payload)


def projects_api_detail(request, slug: str):
    project = project_by_slug(slug)
    return JsonResponse(_project_payload(project))


def team_api_list(request):
    payload = _paginate(request, team_members_active(), _team_payload)
    return JsonResponse(payload)


def achievements_api_list(request):
    payload = _paginate(request, achievements_list(), _achievement_payload)
    return JsonResponse(payload)


def api_schema(request):
    schema = {
        "name": "Portfolio API",
        "version": "v1",
        "pagination": {
            "query_params": {
                "page": "1-based page number",
                "page_size": f"items per page (max {MAX_PAGE_SIZE})",
            }
        },
        "endpoints": {
            "news_list": "/api/v1/news/",
            "news_detail": "/api/v1/news/<slug>/",
            "projects_list": "/api/v1/projects/",
            "projects_detail": "/api/v1/projects/<slug>/",
            "team_list": "/api/v1/team/",
            "achievements_list": "/api/v1/achievements/",
        },
    }
    return JsonResponse(schema)


def api_docs(request):
    return render(request, "api_docs.html")
