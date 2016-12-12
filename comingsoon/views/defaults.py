from django.shortcuts import render
from django.template import loader

from comingsoon.http import HttpResponseSiteDown
from comingsoon.utils.settings import SITEDOWN_503_TEMPLATE

# Create your views here.

"""
    Seeks for the requested URL, redirects if found and if not redirected
    displays 404 Error page
"""

def site_down(request, template=SITEDOWN_503_TEMPLATE):
    return HttpResponseSiteDown(
        loader.render_to_string(
            template,
            {'request_path': request.path,},
        )
    )
