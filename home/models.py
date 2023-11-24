from django.db import models
from django.shortcuts import render
import bugsnag
import requests
from bs4 import BeautifulSoup

from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalManyToManyField
from wagtail.models import Orderable, Page
from modelcluster.fields import ParentalKey
from wagtail.images import get_image_model_string
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.fields import StreamField
from wagtail.snippets.models import register_snippet
# from wagtail.contrib.settings.models import BaseSetting, register_setting
from . blocks import MerchCatalogueBlock, ReleasesCatalogueBlock, LatestReleasesBlock, ArtistsBlock, RosterBlock, LatestMerchBlock, LatestNewsBlock, PlaylistsBlock
from wagtailautocomplete.edit_handlers import AutocompletePanel
from django.core.paginator import Paginator
from django.core.cache import cache
from wagtailcache.cache import WagtailCacheMixin

# ----------------------------------------------

@register_snippet
class Release(ClusterableModel):

    artist = models.CharField(
        null=False,
        blank=False,
        max_length=255
    )

    title = models.CharField(
        null=False,
        blank=False,
        max_length=255
    )

    artwork = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    url = models.URLField(
        blank=False, 
        null=True
    )

    RELEASE_TYPE_CHOICES = [
        ('Single', 'Single'),
        ('EP', 'EP'),
        ('Album', 'Album'),
        ('Compilation', 'Compilation'),
    ]

    release_type = models.CharField(
        max_length=255, 
        choices=RELEASE_TYPE_CHOICES,
        default='Single',
        blank=False, 
        null=True
    )

    RELEASE_LABEL_CHOICES = [
        ('Circus Records', 'Circus Records'),
        ('Circus Electric', 'Circus Electric'),
    ]

    release_label = models.CharField(
        max_length=255, 
        choices=RELEASE_LABEL_CHOICES,
        default='Circus Records',
        blank=False, 
        null=True
    )

    release_date = models.DateField(
        null=True,
        blank=True
    )

    artist_pages = ParentalManyToManyField(
        'home.ArtistPage',
        blank=True,
        related_name='releases'
    )

    live = models.BooleanField(
        default=False,
        null=False,
        blank=True
    )

    panels = [
        FieldPanel('artist'),
        FieldPanel('title'),
        FieldPanel('artwork'),
        FieldPanel('url'),
        FieldPanel('release_type'),
        FieldPanel('release_label'),
        FieldPanel('release_date'),
        AutocompletePanel('artist_pages'),
        FieldPanel('live'),
    ]

    def __str__(self):
        return f'{self.artist} - {self.title}'

# ----------------------------------------------

@register_snippet
class MerchItem(ClusterableModel):

    title = models.CharField(
        null=False,
        blank=False,
        max_length=255
    )

    image = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    url = models.URLField(
        blank=False, 
        null=True
    )

    price = models.CharField(
        null=False,
        blank=False,
        max_length=255
    )

    MERCH_TYPE_CHOICES = [
        ('T-shirt', 'T-shirt'),
        ('Hoodie', 'Hoodie'),
        ('Hat', 'Hat'),
        ('Vinyl', 'Vinyl'),
    ]

    merch_type = models.CharField(
        max_length=255, 
        choices=MERCH_TYPE_CHOICES,
        blank=True, 
        null=True
    )

    artist_pages = ParentalManyToManyField(
        'home.ArtistPage',
        blank=True,
        related_name='+'
    )

    live = models.BooleanField(
        default=False,
        null=False,
        blank=True
    )

    panels = [
        FieldPanel('title'),
        FieldPanel('image'),
        FieldPanel('url'),
        FieldPanel('price'),
        FieldPanel('merch_type'),
        AutocompletePanel('artist_pages'),
        FieldPanel('live'),
    ]

    def __str__(self):
        return f'{self.title} - {self.price}'

# ----------------------------------------------

@register_snippet
class NewsItem(ClusterableModel):

    title = models.CharField(
        null=False,
        blank=False,
        max_length=255
    )

    image = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    url = models.URLField(
        blank=False, 
        null=True
    )

    description = RichTextField(
        null=False,
        blank=False
    )

    artist_pages = ParentalManyToManyField(
        'home.ArtistPage',
        blank=True,
        related_name='+'
    )

    live = models.BooleanField(
        default=False,
        null=False,
        blank=True
    )

    panels = [
        FieldPanel('title'),
        FieldPanel('image'),
        FieldPanel('url'),
        FieldPanel('description'),
        AutocompletePanel('artist_pages'),
        FieldPanel('live'),
    ]

    def __str__(self):
        return f'{self.title}'
    
# ----------------------------------------------

@register_snippet
class Playlist(ClusterableModel, Orderable):

    title = models.CharField(
        null=False,
        blank=False,
        max_length=255
    )

    headline = models.CharField(
        null=False,
        blank=False,
        max_length=255
    )

    url = models.URLField(
        blank=False, 
        null=True
    )

    description = RichTextField(
        null=False,
        blank=False,
        max_length=255
    )

    artist_pages = ParentalManyToManyField(
        'home.ArtistPage',
        blank=True,
        related_name='+'
    )

    live = models.BooleanField(
        default=False,
        null=False,
        blank=True
    )

    panels = [
        FieldPanel('title'),
        FieldPanel('headline'),
        FieldPanel('url'),
        FieldPanel('description'),
        AutocompletePanel('artist_pages'),
        FieldPanel('live'),
    ]

    def __str__(self):
        return f'{self.title}'

# ----------------------------------------------

class HomePageCarouselImages(Orderable):

    page = ParentalKey("home.HomePage", related_name="carousel_images")

    carousel_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    link = models.URLField(blank=True, default='')

    text = models.CharField(
        null=False,
        blank=False,
        default='',
        max_length=255
    )

    TYPE_CHOICES = [
        ('Release', 'Release'),
        ('Merch', 'Merch'),
        ('Playlist', 'Playlist'),
        ('News', 'News'),
    ]

    type = models.CharField(
        max_length=255, 
        choices=TYPE_CHOICES,
        default='News',
        blank=True, 
        null=True
    )

    panels = [FieldPanel("carousel_image"), 
              FieldPanel("link"),
              FieldPanel("text"),
              FieldPanel("type")
    ]

# ----------------------------------------------

class HomePage(WagtailCacheMixin, Page):

    body = StreamField(
    [
        ('latest_releases', LatestReleasesBlock()),
        ('artists', ArtistsBlock()),
        ('latest_merch', LatestMerchBlock()),
        ('news', LatestNewsBlock()),
    ],
    null=True,
    blank=True,
    use_json_field = True
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [InlinePanel("carousel_images", max_num=3, min_num=1, label="Image")],
            heading="Carousel Images"), 
        FieldPanel('body')
    ]

# ----------------------------------------------

class MerchPage(WagtailCacheMixin, Page):
    template = "home/merch.html"

    # merch_catalogue = StreamField(
    # [
    #     ('merch_catalogue', MerchCatalogueBlock())
    # ],
    # null=True,
    # blank=True,
    # use_json_field = True
    # )

    # content_panels = Page.content_panels + [
    #     FieldPanel('merch_catalogue')
    # ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        merch = (
            MerchItem
            .objects
            .filter(live=True)
            .prefetch_related('artist_pages')
        )

        context['merch'] = merch

        return context

# ----------------------------------------------

class ReleasesPage(WagtailCacheMixin, Page):
    template = "home/releases.html"

    # releases_catalogue = StreamField(
    # [
    #     ('releases_catalogue', ReleasesCatalogueBlock())
    # ],
    # null=True,
    # blank=True,
    # use_json_field = True
    # )

    # content_panels = Page.content_panels + [
    #     FieldPanel('releases_catalogue')
    # ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        artists = ArtistPage.objects.exclude(releases=None).live().values('slug', 'title')
        context['artists'] = artists

        filtered_artist = request.GET.get('artist', None)

        current_page = request.GET.get('page', 1)
        release_objs = (
            Release
            .objects
            .filter(live=True)
            .order_by('-release_date')
            .prefetch_related('artist_pages')
        )

        if filtered_artist:
            release_objs = release_objs.filter(artist_pages__slug=filtered_artist)
            context['filtered_artist'] = filtered_artist

        page_obj = Paginator(release_objs, 16)

        context['page_obj'] = page_obj.get_page(current_page)

        return context

# ----------------------------------------------

class AboutPage(WagtailCacheMixin, Page):
    template = "home/about.html"

    mission_statement = RichTextField(blank=False)
    history = RichTextField(blank=False)
    gaming_info = RichTextField(blank=False)

    mission_pic = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    history_pic = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    gaming_pic = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    content_panels = Page.content_panels + [
        FieldPanel('mission_statement'),
        FieldPanel('history'),
        FieldPanel('gaming_info'),
        FieldPanel('mission_pic'),
        FieldPanel('history_pic'),
        FieldPanel('gaming_pic')
    ]

# ----------------------------------------------

class SignupPage(WagtailCacheMixin, Page):
    template = "home/signup.html"

    signup_text = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('signup_text')
    ]

    def get_context(self, request, *args, **kwargs) -> dict:
        context = super().get_context(request, *args, **kwargs)

        context['news'] = NewsItem.objects.filter(
            live=True).order_by('-live')[:5]

        return context

# ----------------------------------------------

class ArtistPage(WagtailCacheMixin, Page):
    template = "home/artist.html"

    photo = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    thumbnail = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    logo = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    songkick_url = models.URLField(
        blank=True, 
        null=True
    )

    bio = RichTextField(
        null=True,
        blank=True,
        max_length=800
    )

    playlist = models.URLField(
        blank=True, 
        null=True
    )

    rss_feed = models.CharField(
        blank=True,
        null=True,
        max_length=255
    )

    instagram = models.URLField(
        blank=True, 
        null=True
    )

    spotify = models.URLField(
        blank=True, 
        null=True
    )

    apple_music = models.URLField(
        blank=True, 
        null=True
    )

    tiktok = models.URLField(
        blank=True, 
        null=True
    )  

    twitter = models.URLField(
        blank=True, 
        null=True
    ) 

    content_panels = Page.content_panels + [
        FieldPanel('photo'),
        FieldPanel('thumbnail'),
        FieldPanel('logo'),
        FieldPanel('songkick_url'),
        FieldPanel('rss_feed'),
        FieldPanel('bio'),
        FieldPanel('playlist'),
        FieldPanel('instagram'),
        FieldPanel('spotify'),
        FieldPanel('apple_music'),
        FieldPanel('tiktok'),
        FieldPanel('twitter'),
    ]

    def get_events_from_songkick(self):
        try:
            response = requests.get(self.songkick_url)
            assert response.status_code == 200
            content = response.content
        except Exception as e:
            bugsnag.notify(e)
            return []
            
        soup = BeautifulSoup(content, 'html.parser')
        calendar = soup.find(id="calendar-summary")
        events = []

        if calendar:
            
            listings = calendar.find_all(class_="event-listing")

            for event in listings:
                event_list = []

                city = event.find(class_='primary-detail')
                event_list.append(city.text)

                venue = event.find(class_='secondary-detail')
                event_list.append(venue.text)

                month = event.find(class_='month')
                event_list.append(month.text)

                date = event.find(class_='date')
                event_list.append(date.text.strip())

                link = event.a
                event_list.append("https://www.songkick.com/" + link.get('href'))

                events.append(event_list)

        return events
    
    def get_events(self):
        cache_key = f'events_for_{self.slug}'
        cached_data = cache.get(cache_key)
        if not cached_data:
            data = self.get_events_from_songkick()
            cache.set(cache_key, data, 3600) # hour
            return data

        return cached_data

    def get_context(self, request, *args, **kwargs) -> dict:
        context = super().get_context(request, *args, **kwargs)

        if self.songkick_url:
            events = self.get_events()
            
            context['listings'] = events

        context['releases'] = Release.objects.filter(
            artist_pages=self, live=True).order_by('-release_date')[:4]
        
        context['merch'] = MerchItem.objects.filter(
            artist_pages=self, live=True).order_by('-live')[:4]

        context['news'] = NewsItem.objects.filter(
            artist_pages=self, live=True).order_by('-live')[:2]
        
        # context['playlist'] = Playlist.objects.filter(
        #     artist_pages=self, live=True).order_by('-live')

        return context

# ----------------------------------------------

class RosterPage(WagtailCacheMixin, Page):
    template = "home/roster.html"

    # body = StreamField(
    # [
    #     ('artists', RosterBlock()),
    # ],
    # null=True,
    # blank=True,
    # use_json_field = True
    # )

    # content_panels = Page.content_panels + [
    #     FieldPanel('body')
    # ]
    def get_context(self, request, *args, **kwargs) -> dict:
        context = super().get_context(request, *args, **kwargs)
        artists = ArtistPage.objects.live().order_by('title')
        context['artists'] = artists
        return context
# ----------------------------------------------

class PlaylistPage(WagtailCacheMixin, Page):
    template = "home/playlists.html"

    body = StreamField(
    [
        ('playlists', PlaylistsBlock()),
    ],
    null=True,
    blank=False,
    use_json_field = True
    )

    content_panels = Page.content_panels + [
        FieldPanel('body')
    ]

# ----------------------------------------------

class ContactPage(WagtailCacheMixin, Page):
    template = "home/contact.html"

# ----------------------------------------------

class CookiePolicy(WagtailCacheMixin, Page):
    template = "home/cookie_policy.html"

# ----------------------------------------------

class TermsConditions(WagtailCacheMixin, Page):
    template = "home/terms_conditions.html"

# ----------------------------------------------

class PrivacyPolicy(WagtailCacheMixin, Page):
    template = "home/privacy_policy.html"