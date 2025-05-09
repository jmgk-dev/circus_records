# Music label site / circus-records.co.uk

## Description
Wagtail site created for a electronic music label. Has the functionality to add artists, releases, news items, merch items and live dates as well as a dynamic homepage banner and customisable about and 'sign up' pages.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Contact Information](#contact-information)

## Installation

# Clone the repo
```bash
git clone https://github.com/jmgk-dev/circus_records.git
```

# Navigate to the project directory
```bash
cd circus_records
```

# Create a virtual environment
```bash
python3 -m venv venv
```

# Activate the virtual environment
```bash
source venv/bin/activate
```

# Create superuser
```bash
python manage.py createsuperuser
```

# Install dependencies
```bash
pip install -r requirements.txt
```

# Create a secret keys for development and production to a new .env
```bash
echo "DJANGO_DEV_KEY=$(python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')" >> .env && \
echo "DJANGO_SECURE_PRODUCTION_KEY=$(python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')" >> .env
```

# Migrate the database
```bash
python manage.py migrate
```

# Start the development server
```bash
python manage.py runserver
```


## Usage
Instructions on how to use the project.

It's advisable to start by adding an artist, as all other relevant items can be then tagged to the artist.

## Contact Information
```
jamie@jmgk.dev
```

