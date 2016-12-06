from django.conf.urls import *
from django.views.generic import TemplateView
from . import views
from .views import ComingView, comingsoon

urlpatterns = [
        #url('^.*$', ComingView.as_view(), name='comingsoon'),
        url('^.*$', views.comingsoon, name='comingsoon'),
]
