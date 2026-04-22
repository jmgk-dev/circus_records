from wagtail import hooks
from wagtailcache.cache import clear_cache

# Flush the full page cache whenever a live page is created or edited.
# We clear everything rather than just the edited page because blocks like
# LatestReleasesBlock can surface content from any page across the site —
# a release update on one artist page would otherwise leave stale data on
# the homepage and other aggregate views.
@hooks.register('after_create_page')
@hooks.register('after_edit_page')
def clear_wagtailcache(request, page):
    if page.live:
        clear_cache()