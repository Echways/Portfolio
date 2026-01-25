from django.shortcuts import get_object_or_404

from info.models import Project


def projects_list():
    return Project.objects.all()


def project_by_slug(slug: str):
    return get_object_or_404(Project, slug=slug)
