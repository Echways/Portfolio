from django.views.generic import ListView

from info.achievements.selectors import achievements_list
from info.team.selectors import team_members_active


class InfoPageView(ListView):
    template_name = "info/infopage.html"

    def get_queryset(self):
        return achievements_list()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["team_members"] = team_members_active()
        return context
