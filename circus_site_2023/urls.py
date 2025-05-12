from django.conf import settings
from django.http import HttpResponse
from django.urls import include, path
from django.contrib import admin
from django.views.decorators.cache import cache_page

from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from django.contrib.sitemaps.views import sitemap
from home.sitemaps import WagtailSitemap

from search import views as search_views
from wagtailautocomplete.urls.admin import urlpatterns as autocomplete_admin_urls

sitemaps = {
    'pages': WagtailSitemap(),
}

@cache_page(60 * 60 * 24)
def robots_txt(request):
    lines = [
        "User-agent: *",
        "Disallow: /admin/",
        "Sitemap: https://circus-records.co.uk/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")

urlpatterns = [
    path("django-admin/", admin.site.urls),
    path("admin/autocomplete/", include(autocomplete_admin_urls)),
    path("admin/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
    path("search/", search_views.search, name="search"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path("robots.txt", robots_txt, name="robots_txt"),
    path("", include(wagtail_urls)),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


