from django import template
from home.models import MerchItem, Release, Playlist

register = template.Library()

# Merch Item snippets
@register.inclusion_tag('tags/merch_tag.html', takes_context=True)
def merch_items(context):
    return {
        'merch_items': MerchItem.objects.all(),
        'request': context['request'],
    }

# Release snippets
@register.inclusion_tag('tags/release_tag.html', takes_context=True)
def releases(context):
    return {
        'releases': Release.objects.all(),
        'request': context['request'],
    }

# Playlist snippets
@register.inclusion_tag('tags/playlist_tag.html', takes_context=True)
def playlists(context):
    return {
        'playlists': Playlist.objects.all(),
        'request': context['request'],
    }