from django.db import models
from django.shortcuts import render

import requests
from bs4 import BeautifulSoup

from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalManyToManyField
from wagtail.models import Orderable, Page
from modelcluster.fields import ParentalKey
from wagtail.images import get_image_model_string
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.core.fields import StreamField
from wagtail.snippets.models import register_snippet
from wagtail.contrib.settings.models import BaseSetting, register_setting
from .blocks import MerchCatalogueBlock, ReleasesCatalogueBlock, LatestReleasesBlock, ArtistsBlock, RosterBlock, LatestMerchBlock, LatestNewsBlock
from wagtailautocomplete.edit_handlers import AutocompletePanel

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
        max_length=11, 
        choices=RELEASE_TYPE_CHOICES,
        default='Single',
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
        max_length=11, 
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

    panels = [FieldPanel("carousel_image"), FieldPanel("link")]


# ----------------------------------------------

class HomePage(Page):

    body = StreamField(
    [
        ('latest_releases', LatestReleasesBlock()),
        ('artists', ArtistsBlock()),
        ('latest_merch', LatestMerchBlock()),
        ('news', LatestNewsBlock()),
    ],
    null=True,
    blank=False,
    use_json_field = True
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [InlinePanel("carousel_images", max_num=3, min_num=1, label="Image")],
            heading="Carousel Images"), 
        FieldPanel('body')
    ]

# ----------------------------------------------

class MerchPage(Page):
    template = "home/merch.html"

    merch_catalogue = StreamField(
    [
        ('merch_catalogue', MerchCatalogueBlock())
    ],
    null=True,
    blank=False,
    use_json_field = True
    )

    content_panels = Page.content_panels + [
        FieldPanel('merch_catalogue')
    ]

# ----------------------------------------------

class ReleasesPage(Page):
    template = "home/releases.html"

    releases_catalogue = StreamField(
    [
        ('releases_catalogue', ReleasesCatalogueBlock())
    ],
    null=True,
    blank=False,
    use_json_field = True
    )

    content_panels = Page.content_panels + [
        FieldPanel('releases_catalogue')
    ]

# ----------------------------------------------

class AboutPage(Page):
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

class SignupPage(Page):
    template = "home/signup.html"

    signup_text = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('signup_text')
    ]

# ----------------------------------------------

class ArtistPage(Page):
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

    bio = RichTextField(
        null=True,
        blank=True,
        max_length=800
    )

    content_panels = Page.content_panels + [
        FieldPanel('photo'),
        FieldPanel('thumbnail'),
        FieldPanel('logo'),
        FieldPanel('bio'),
    ]


    def get_context(self, request, *args, **kwargs) -> dict:
        context = super().get_context(request, *args, **kwargs)

        response = requests.get("https://www.songkick.com/artists/1845075-flux-pavilion/calendar")

        if response.status_code != 200:
            print("Error fetching page")
            exit()
        else:
            content = response.content
                
        soup = BeautifulSoup(response.content, 'html.parser')
        calendar = soup.find(id="calendar-summary")
        listings = calendar.find_all(class_="event-listing")
        list = []

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

            list.append(event_list)

        context['listings'] = list

        return context


# ----------------------------------------------

class RosterPage(Page):
    template = "home/roster.html"

    body = StreamField(
    [
        ('artists', RosterBlock()),
    ],
    null=True,
    blank=False,
    use_json_field = True
    )

    content_panels = Page.content_panels + [
        FieldPanel('body')
    ]
       
# ----------------------------------------------

class PlaylistPage(Page):
    template = "home/playlists.html"

class ContactPage(Page):
    template = "home/contact.html"