from wagtail.core import blocks

from wagtail.images.blocks import ImageChooserBlock

# ----------------------------------------------

class ReleaseBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=True)
    link = blocks.URLBlock(required=True)
    artist = blocks.CharBlock(required=True)
    title = blocks.CharBlock(required=True)
    type = blocks.CharBlock(required=False)

class ReleasesCatalogueBlock(blocks.StructBlock):

    class Meta:
        template = 'blocks/releases_catalogue.html'

    releases = blocks.ListBlock(
        ReleaseBlock()
    )

# ----------------------------------------------

class ArtistsBlock(blocks.StructBlock):
    class Meta:
        icon = 'star'
        template = 'blocks/artists.html'
        
    artists = blocks.ListBlock(
        blocks.PageChooserBlock('home.ArtistPage', required=True),
        required=True
    )

# ----------------------------------------------

class RosterBlock(blocks.StructBlock):
    class Meta:
        icon = 'star'
        template = 'blocks/roster_list.html'
    
    artists = blocks.ListBlock(
        blocks.PageChooserBlock('home.ArtistPage', required=True),
        required=True
    )
    
# ----------------------------------------------

class LatestReleasesBlock(blocks.StructBlock):
    class Meta:
        icon = 'star'
        template = 'blocks/latest_releases.html'

    title = blocks.CharBlock(required=False, default="Latest Releases")
    limit = blocks.IntegerBlock(label="Show maximum", required=True, default=3)

    def get_context(self, value, parent_context=None):
        from .models import Release
        context = super().get_context(value, parent_context=parent_context)

        context['latest_releases'] = (
            Release
            .objects
            .filter(live=True)
            .prefetch_related('artist_pages')
            .order_by('-release_date')
        )[:value['limit']]

        return context

# ----------------------------------------------


class MerchBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=True)
    link = blocks.URLBlock(required=True)
    description = blocks.CharBlock(required=True)
    type = blocks.CharBlock(required=True)
    price = blocks.CharBlock(required=True)

class MerchCatalogueBlock(blocks.StructBlock):

    class Meta:
        template = 'blocks/merch_catalogue.html'

    merch = blocks.ListBlock(
        MerchBlock()
    )

# ----------------------------------------------

class LatestMerchBlock(blocks.StructBlock):
    class Meta:
        icon = 'star'
        template = 'blocks/latest_merch.html'

    title = blocks.CharBlock(required=False, default="Latest Merch")
    limit = blocks.IntegerBlock(label="Show maximum", required=True, default=3)

    def get_context(self, value, parent_context=None):
        from .models import MerchItem
        context = super().get_context(value, parent_context=parent_context)

        context['latest_merch'] = (
            MerchItem
            .objects
            .filter(live=True)
            .order_by('-live')
        )[:value['limit']]

        return context
    
# ----------------------------------------------

class LatestNewsBlock(blocks.StructBlock):
    class Meta:
        icon = 'star'
        template = 'blocks/latest_news.html'
        
    title = blocks.CharBlock(required=False, default="Latest Merch")
    limit = blocks.IntegerBlock(label="Show maximum", required=True, default=2)

    def get_context(self, value, parent_context=None):
        from .models import NewsItem
        context = super().get_context(value, parent_context=parent_context)

        context['latest_news'] = (
            NewsItem
            .objects
            .filter(live=True)
            .prefetch_related('artist_pages')
            .order_by('-live')
        )[:value['limit']]

        return context