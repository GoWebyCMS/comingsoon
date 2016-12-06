from django.db import models
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Maintenance(models.Model):
    name = models.CharField(max_length=200)
    content = RichTextField()

    active = models.BooleanField('In Maintenance Mode', default=False)
    start = models.DateTimeField(blank=True)
    end = models.DateTimeField(blank=True)

    class Meta:
        verbose_name_plural = "under construction"

    def __str__(self):
        return self.name

class IgnoredURL(models.Model):
    maintenance = models.ForeignKey(Maintenance)
    pattern = models.CharField(max_length=255)
    description = models.CharField(max_length=75, help_text='What this URL pattern covers.')

    def __str__(self):
        return self.pattern
