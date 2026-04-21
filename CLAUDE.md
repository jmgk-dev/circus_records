# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Wagtail CMS website for Circus Records, an electronic music label (circus-records.co.uk). All content is managed via the Wagtail admin.

## Common Commands

```bash
# Dev server
python manage.py runserver

# Database
python manage.py migrate
python manage.py createsuperuser

# Tests
python manage.py test
python manage.py test home.tests.LiveDateModelTest  # single test class

# Static files (needed after changes)
python manage.py collectstatic
```

## Settings & Environment

Settings are split into `circus_site_2023/settings/base.py`, `dev.py`, and `production.py`. The `SERVER_ENV` environment variable (or its absence) controls which settings module `manage.py` loads — dev by default.

Required `.env` variables:
- `DJANGO_DEV_KEY` — dev secret key
- `SECURE_PRODUCTION_KEY` — production secret key
- Production also requires: `DB_NAME/DB_USER/DB_PASSWORD`, `AWS_S3_ACCESS_KEY_ID/AWS_SECRET_ACCESS_KEY`, `EMAIL_HOST_*`, `BUGSNAG_API_KEY`, and various analytics IDs

Dev uses SQLite; production uses PostgreSQL + DigitalOcean Spaces for media via django-storages.

## Architecture

### App Structure

- **`home/`** — contains essentially all of the site's logic: models, StreamField blocks, template tags, Wagtail hooks, sitemaps, and tests
- **`search/`** — single view for site-wide search with pagination
- **`circus_site_2023/`** — project config (settings, URLs, context processors, base templates)

### URL Routing

- `/admin/` → Wagtail admin
- `/django-admin/` → Django admin
- `/search/` → search view
- `/sitemap.xml` → Wagtail sitemap
- Everything else → Wagtail page tree

### Models (`home/models.py`)

**Snippet models** (Wagtail-registered, edited in admin):
- `LiveDate` — live events (date, venue, ticket link, artist tag)
- `Release` — music releases (type: Single/EP/Album/Compilation, label, artwork)
- `MerchItem` — merchandise (type: T-shirt/Hoodie/Hat/Vinyl, price, image)
- `NewsItem` — news articles
- `Playlist` — music playlists with embed links

**Page models** (Wagtail page tree):
- `HomePage` — carousel images + StreamField content blocks
- `ArtistPage` — artist profile with social links and associated snippets
- `ReleasesPage` — paginated releases (16/page) with artist filtering
- `RosterPage`, `MerchPage`, `PlaylistPage`, `AboutPage`, `ContactPage`, `SignupPage`, `CookiePolicy`, `TermsConditions`

All page models use `WagtailCacheMixin` (1-week TTL, file-based cache in `/cache/`).

### StreamField Blocks (`home/blocks.py`)

Blocks used in `HomePage` and other pages to compose content: `LatestReleasesBlock`, `LatestMerchBlock`, `LatestNewsBlock`, `ArtistsBlock`, `RosterBlock`, `PlaylistsBlock`, `ReleasesCatalogueBlock`, `MerchCatalogueBlock`.

### Frontend

No JS build toolchain — static assets live in `/staticfiles/` (committed to the repo). Templates use Django template language. Custom template tags in `home/templatetags/home_tags.py` handle merch, release, and playlist inclusion tags. Slick carousel is used for image sliders.
