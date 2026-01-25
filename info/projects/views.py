from django.views.generic import DetailView, ListView

from info.models import Project
from info.projects.selectors import project_by_slug, projects_list


class ProjectListView(ListView):
    template_name = "info/projects.html"
    paginate_by = 6

    def get_queryset(self):
        return projects_list()


class ProjectDetailView(DetailView):
    model = Project
    template_name = "info/projectpost_dl.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_object(self, queryset=None):
        return project_by_slug(self.kwargs["slug"])
