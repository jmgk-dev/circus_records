from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
    
class RosterPage(Page):
    template = "home/roster.html"

class ArtistPage(Page):
    template = "home/artist.html"

class MerchPage(Page):
    template = "home/merch.html"

class PlaylistPage(Page):
    template = "home/playlists.html"