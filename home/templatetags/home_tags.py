from django import template
from home.models import MerchItem, Release

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

# Artist Release snippets
@register.inclusion_tag('tags/artist_release_tag.html', takes_context=True)
def artist_releases(context):
    return {
        'releases': Release.objects.all(),
        'request': context['request'],
    }

# Artist Merch snippets
@register.inclusion_tag('tags/artist_merch_tag.html', takes_context=True)
def artist_merch_items(context):
    return {
        'merch_items': MerchItem.objects.all(),
        'request': context['request'],
    }