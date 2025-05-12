from django.contrib.sitemaps import Sitemap
from wagtail.models import Page
from wagtail.models import Site

class WagtailSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        # Return all live, public pages
        return Page.objects.live().public().specific()

    def location(self, item):
        # Dynamically determine the site's root URL
        current_site = Site.find_for_request(None)  # Automatically detects the current site
        if current_site:
            return f"{current_site.root_url}{item.url}"
        return item.get_full_url()

    def lastmod(self, item):
        # Use the last published or modified date
        return item.latest_revision_created_at