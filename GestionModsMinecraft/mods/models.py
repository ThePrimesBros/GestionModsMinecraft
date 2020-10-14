from django.db import models# Create your models here.

class Mods(models.Model):

    title = models.CharField(max_length=200)
    creator = models.CharField(max_length=255, default="", unique=True)   
    description = models.TextField(default="", blank=True, null=True)
    version = models.CharField(max_length=30, default="", blank=True, null=True)  
    download = models.CharField(max_length=255, default="", blank=True, null=True)
    img = models.CharField(max_length=255, default="", blank=True, null=True)