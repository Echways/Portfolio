from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", include("config.urls.admin")),
    path("", include("config.urls.public")),
]

handler404 = "config.core.views.handler404"
handler500 = "config.core.views.handler500"

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
