from django.contrib import admin

from mods.models import News

class NewsAdmin(admin.ModelAdmin):
    list_display=('title','link')
    
admin.site.register(News, NewsAdmin)
