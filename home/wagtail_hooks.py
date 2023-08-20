from django.core.cache import cache
from wagtail import hooks
from wagtailcache.cache import clear_cache

@hooks.register('after_create_page')
@hooks.register('after_edit_page')
def clear_wagtailcache(request, page):
    if page.live:
        cache.delete(f'events_for_{page.slug}')
        clear_cache()