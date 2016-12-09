# Coming Soon Django Application
## Initially developed for Django Hatchery CMS

[![Build Status]

Current Version: 0.0

This django application makes it easy to put your Django site into "under construction mode", or more technically, return an HTTP 503 response.

The coming soon falg is stord in the projects database as a BoolianField. That makes it easy to enable/disable

## Requirements
- [django](https://www.djangoproject.com/download/)
- [django.contrib.sites](https://docs.djangoproject.com/en/1.8/ref/contrib/sites/)

## Pre-Requisites
You must have at least one Site entry in your database **before** installing Comingsoon.

## Supported Django Versions
- 1.9
- 1.8
- 1.7
- 1.6
- 1.5 or below *should* work, but come on, it's time to upgrade :)

## Installation
TODO: configure installation via pip
- `pip install comingsoon`

-- or --

Download Coming Soon from [source](https://github.com/)

Enable a virtualenv

  - $ virtualenv virtualenv
  - $ source venv/bin/activate

Python Setup  
  - $ python setup.py install
  or
  - add `comingsoon` to your PYTHONPATH

## Settings and Required Values
- Ensure the [Sites Framework](https://docs.djangoproject.com/en/1.8/ref/contrib/sites/) is enabled and that you have at least one entry in the Sites table.
- Add `comingsoon.middleware.ComingsoonModeMiddleware` to your `MIDDLEWARE_CLASSES`
- Add `comingsoon` to your `INSTALLED_APPS`
- Run `python manage.py migrate` to create the `comingsoon` database tables.
- Run your project to automatically add the `comingsoon` database records.
- Add a 503.html template to the root of your templates directory, or optionally add a `COMINSOON_503_TEMPLATE` path to your 503.html file's location in settings.
- `comingsoon` will ignore any patterns beginning with the default Django Admin url: `^admin` so you can turn it off. If you use a custom url for admin, you may override the ignored admin patterns by adding the ` COMINGSOON_ADMIN_IGNORED_URLS` list in settings.
Example: `['^my-custom-admin', '^my-other-custom-admin']`

## Usage
TODO: Add usage screen and description

### Turning Comingsoon Mode **On**
To put a site into "Comingsoon Mode", just check the "Comingsoon Mode" checkbox and save in Django Admin under the "Coming Soon" section. The next time you visit the public side of the site it will return a 503 if:

- You are not logged in as a superuser or staff user
- You are not viewing a URL in the ignored patterns list
- Your `REMOTE_ADDR` does not appear in the `INTERNAL_IPS` setting

### Turning Comingsoon Mode **Off**
Just log in, un-check the "Coming Soon Mode" checkbox and save.

### Database migrations
  `manage.py migrate`

  TODO: Legacy support for South migrations
