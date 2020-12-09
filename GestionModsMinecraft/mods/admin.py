from django.contrib import admin
from mods.models import Version
from mods.models import Mods

class ModsAdmin(admin.ModelAdmin):
    list_display=('title','creator', 'version')



    
admin.site.register(Mods, ModsAdmin)
admin.site.register(Version)
