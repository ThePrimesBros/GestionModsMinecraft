from django.contrib import admin

from mods.models import Mods

class ModsAdmin(admin.ModelAdmin):
    list_display=('name','created_date', 'creator', 'mod_type')
    
admin.site.register(Mods, ModsAdmin)
