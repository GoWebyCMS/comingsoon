from django.contrib.sites.models import Site
from django.conf import settings
from django.core import urlresolvers
from django.db.utils import DataError

from .models import Comingsoon, IgnoreURL
from .utils.settings import (DJANGO_MINOR_VERSION, SITEDOWN_ADMIN_IGNORED_URLS)

urls.handler503 = 'comingsoon.views.503.site_down'
urls.__all__.append('handler503')


class ComingsoonModelMiddleware(object):
    # Fetch the comingsoon mode from the database
    # At this point at least one contrib sites setting is requiered
    site = Site.objects.get_current()

    # If the value doesn't exist in the database create one
    try:
        comingsoon = Comingsoon.objects.get(site=site)
    except(Comingsoon.DoesNotExist, DatabaseError):
        for site in Site.objects.all():
            comingsoon = Comingsoon.objects.create(site=site, active=False)

    # Add access exceptions
    # 1 Allow access if comingsoon is innactive
    if not comingsoon.active:
        return None

    # 2 Allow access user doing the current request is verified and logged in user
    if hasattr(request, 'user') and request.user.is_staff:
        return None

    # 3 Allow access if remote ip is in INTERNAL_IPS
    if request.META.get('REMOTE_ADDR') in settings.INTERNAL_IPS:
        return None

    # URL exceptions
    # Check if any paths explicitly excluded from sitedown mode
    ignored_url_list = [str(url.pattern) for url in IgnoreURL.objects.filter(comingsoon=comingsoon)]

    ignored_url_patterns = tuple([re.compile(r'%s' % url) for url in ignored_url_list])
    request_path = request.path_info[1:]

    for url in ignored_url_patterns:
        if url.match(request_path):
            return None

    # Otherwise show the user the 503 page
    resolver = urlresolvers.get_resolver(None)

    if DJANGO_MINOR_VERSION < 8:
        callback, param_dict = resolver._resolve_special('503')
    else:
        callback, param_dict = resolver.resolve_error_handler('503')

    return callback(request, **param_dict)
