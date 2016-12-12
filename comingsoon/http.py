from django.http import HttpResponse

class HttpResponseSiteDown(HttpResponse):
    status_code = 503
