from django.test import TestCase
from django.contrib.auth import get_user_model
from wagtail.images.models import Image
from wagtail.images.tests.utils import get_test_image_file
from home.models import LiveDate, Release, MerchItem, NewsItem, Playlist, HomePage, HomePageCarouselImages
from wagtail.models import Site, Page

User = get_user_model()

class LiveDateModelTest(TestCase):

    def setUp(self):
        self.artist_page = Site.objects.create(
            hostname='example.com',
            port=80,
            site_name='Test Site',
            root_page=HomePage.objects.first(),
            is_default_site=True
        )

    def test_create_live_date(self):
        live_date = LiveDate.objects.create(
            event_name="Test Event",
            venue="Test Venue",
            date="2025-04-08",
            ticket_link="http://example.com",
            live=True
        )
        live_date.artist_pages.add(self.artist_page.root_page)
        self.assertEqual(str(live_date), "Test Event - Test Venue - 2025-04-08")


class ReleaseModelTest(TestCase):

    def setUp(self):
        self.artist_page = Site.objects.create(
            hostname='example.com',
            port=80,
            site_name='Test Site',
            root_page=HomePage.objects.first(),
            is_default_site=True
        )
        self.image = Image.objects.create(
            title='Test Image',
            file=get_test_image_file()
        )

    def test_create_release(self):
        release = Release.objects.create(
            artist="Test Artist",
            title="Test Title",
            artwork=self.image,
            url="http://example.com",
            release_type="Single",
            release_label="Circus Records",
            release_date="2025-04-08",
            live=True
        )
        release.artist_pages.add(self.artist_page.root_page)
        self.assertEqual(str(release), "Test Artist - Test Title")


class MerchItemModelTest(TestCase):

    def setUp(self):
        self.artist_page = Site.objects.create(
            hostname='example.com',
            port=80,
            site_name='Test Site',
            root_page=HomePage.objects.first(),
            is_default_site=True
        )
        self.image = Image.objects.create(
            title='Test Image',
            file=get_test_image_file()
        )

    def test_create_merch_item(self):
        merch_item = MerchItem.objects.create(
            title="Test Merch",
            image=self.image,
            url="http://example.com",
            price="20.00",
            merch_type="T-shirt",
            live=True
        )
        merch_item.artist_pages.add(self.artist_page.root_page)
        self.assertEqual(str(merch_item), "Test Merch - 20.00")


class NewsItemModelTest(TestCase):

    def setUp(self):
        self.artist_page = Site.objects.create(
            hostname='example.com',
            port=80,
            site_name='Test Site',
            root_page=HomePage.objects.first(),
            is_default_site=True
        )
        self.image = Image.objects.create(
            title='Test Image',
            file=get_test_image_file()
        )

    def test_create_news_item(self):
        news_item = NewsItem.objects.create(
            title="Test News",
            image=self.image,
            url="http://example.com",
            description="Test Description",
            live=True
        )
        news_item.artist_pages.add(self.artist_page.root_page)
        self.assertEqual(str(news_item), "Test News")


class PlaylistModelTest(TestCase):

    def setUp(self):
        self.artist_page = Site.objects.create(
            hostname='example.com',
            port=80,
            site_name='Test Site',
            root_page=HomePage.objects.first(),
            is_default_site=True
        )

    def test_create_playlist(self):
        playlist = Playlist.objects.create(
            title="Test Playlist",
            headline="Test Headline",
            url="http://example.com",
            description="Test Description",
            live=True
        )
        playlist.artist_pages.add(self.artist_page.root_page)
        self.assertEqual(str(playlist), "Test Playlist")


class HomePageModelTest(TestCase):

    def setUp(self):
        # Create a root page if it doesn't exist
        if not Page.objects.filter(slug='root').exists():
            root_page = Page(title='Root', slug='root')
            Page.objects.create(
                title='Root',
                slug='root'
            )
            root_page.save_revision().publish()
        else:
            root_page = Page.objects.get(slug='root')

        self.home_page = HomePage(title="Home", slug="home-test")
        root_page.add_child(instance=self.home_page)
        self.home_page.save_revision().publish()

        self.image = Image.objects.create(
            title='Test Image',
            file=get_test_image_file()
        )

    def test_create_home_page(self):
        self.assertEqual(self.home_page.title, "Home")

    def test_add_carousel_image(self):
        carousel_image = HomePageCarouselImages.objects.create(
            page=self.home_page,
            carousel_image=self.image,
            link="http://example.com",
            text="Test Image",
            type="Release"
        )
        self.assertEqual(carousel_image.text, "Test Image")