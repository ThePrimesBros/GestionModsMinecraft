from django.db import models# Create your models here.

class Mods(models.Model):

    title = models.CharField(max_length=200, unique=True)
    creator = models.CharField(max_length=255, default="")   
    description = models.TextField(default="", blank=True, null=True)
    version = models.CharField(max_length=30, default="", blank=True, null=True)  
    download = models.CharField(max_length=255, default="", blank=True, null=True)
    img = models.CharField(max_length=255, default="", blank=True, null=True)

class Version(models.Model):

    version = models.CharField(max_length=30, default="", unique=True, null=True)