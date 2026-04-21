# Circus Records

CMS-driven website for [Circus Records](https://circus-records.co.uk), a UK electronic music label. Built with Wagtail on top of Django, it gives the label full editorial control over artists, releases, merchandise, news, live dates, and playlists — all without touching code.

## Tech Stack

- **[Wagtail](https://wagtail.org/)** — CMS framework (page tree, StreamField, snippets, image management)
- **[Django](https://www.djangoproject.com/)** 5.2 — web framework
- **PostgreSQL** — production database (SQLite in development)
- **[DigitalOcean Spaces](https://www.digitalocean.com/products/spaces)** — media storage (S3-compatible, via django-storages)
- **[WhiteNoise](https://whitenoise.readthedocs.io/)** — static file serving
- **[wagtail-cache](https://github.com/coderedcorp/wagtail-cache)** — full-page response caching (1-week TTL, auto-invalidated on publish)
- **[Bugsnag](https://www.bugsnag.com/)** — error monitoring in production

## Features

- **Artist pages** — bio, press shot, social links (Instagram, Spotify, Apple Music, TikTok, Twitter), embedded playlist, and auto-populated releases/merch/news/live dates
- **Releases** — filterable, paginated catalogue with artist association and release type (Single/EP/Album/Compilation)
- **Merchandise** — per-item type, price, and artist tagging
- **Live dates** — per-artist event listings with venue, date, and ticketing link
- **News** — rich-text articles with artist tagging
- **Playlists** — embed-based playlist showcase
- **Dynamic homepage** — editor-composed via StreamField blocks (latest releases, artists, merch, news)
- **Site search** — full-text search across all live pages with hit tracking for content analytics
- **SEO** — XML sitemap, robots.txt, Google Analytics, Meta Pixel, MailerLite signup integration

## Architecture

Content is split into two categories:

**Snippets** (`LiveDate`, `Release`, `MerchItem`, `NewsItem`, `Playlist`) are standalone objects managed in the Wagtail admin. Each has a `live` boolean toggle that controls frontend visibility independently of the page tree. Snippets are linked to one or more `ArtistPage` instances via `ParentalManyToManyField`, which allows them to appear on individual artist pages as well as in sitewide aggregate views.

**Pages** sit in Wagtail's page tree and handle URL routing automatically. `HomePage` and `PlaylistPage` use StreamField to let editors compose their layout from a palette of content blocks. All page models mix in `WagtailCacheMixin` for full-page caching; a Wagtail hook flushes the cache on every publish.

```
circus_records/
├── home/                   # All models, blocks, template tags, hooks, tests
├── search/                 # Site search view
└── circus_site_2023/       # Project settings, URLs, context processors
    └── settings/
        ├── base.py         # Shared config
        ├── dev.py          # SQLite, debug toolbar, console email
        └── production.py   # PostgreSQL, S3, SSL, Bugsnag
```

## Local Setup

```bash
git clone https://github.com/jmgk-dev/circus_records.git
cd circus_records
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file with a development secret key:

```bash
echo "DJANGO_DEV_KEY=$(python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')" >> .env
```

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

The admin is at `http://127.0.0.1:8000/admin/`. Start by creating an Artist page — releases, merch, news, and live dates can then be tagged to it from their respective snippet editors.

## Contact

jamie@jmgk.dev
