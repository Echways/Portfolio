from django.views.generic import DetailView, ListView

from info.models import News
from info.news.selectors import news_by_slug, news_list


class NewsListView(ListView):
    template_name = "info/news.html"
    paginate_by = 6

    def get_queryset(self):
        return news_list()


class NewsDetailView(DetailView):
    model = News
    template_name = "info/newspost_dl.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_object(self, queryset=None):
        return news_by_slug(self.kwargs["slug"])
