from django.db import models
from datetime import date, timedelta
from django.utils.html import format_html

class Mods(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    created_date = models.DateField(null=True)
    creator = models.CharField(max_length=250)
    last_maj = models.DateField(null=True)
    version = models.CharField(max_length=250)
    mod_type = models.CharField(max_length=250)
    download = models.TextField()
