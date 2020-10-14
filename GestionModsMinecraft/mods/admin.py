from django.contrib import admin

from mods.models import Mods

class ModsAdmin(admin.ModelAdmin):
    list_display=('title','link')
    
admin.site.register(Mods, ModsAdmin)
