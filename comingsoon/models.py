from django.db import models
from django.contrib.sites.models import Site

# Create your models here.

class Comingsoon(models.Model):
    name = models.CharField(max_length=255)
    site = models.ForeignKey(Site, null=True, blank=True)
    active = models.BooleanField('Coming Soon Mode', default=False)
    # count down fields
    start = models.DateTimeField(blank=True)
    end = models.DateTimeField(blank=True)

    class Meta:
        verbose_name = 'Coming Soon'
        verbose_name_plural = 'Coming Soon'

    def __str__(self):
        return self.name

class IgnoreURL(models.Model):
    comingsoon = models.ForeignKey(Comingsoon)
    pattern = models.CharField(max_length=200)
    about = models.CharField(max_length=100, help_text="About this URL")

    def __str__(self):
        return self.pattern
