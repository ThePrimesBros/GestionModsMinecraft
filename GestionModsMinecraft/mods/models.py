from django.db import models# Create your models here.

class Mods(models.Model):

    title = models.CharField(max_length=200)
    creator = models.CharField(max_length=2083, default="", unique=True)   
    created_date = models.DateTimeField()   
    last_maj = models.DateTimeField(auto_now_add=True)   
    version = models.CharField(max_length=30, default="", blank=True, null=True)  
    download = models.CharField(max_length=30, default="", blank=True, null=True)
    img = models.CharField(max_length=30, default="", blank=True, null=True)