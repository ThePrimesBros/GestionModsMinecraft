from django.shortcuts import render
from django.http import HttpResponse
from mods.models import Mods


def mods_listing(request):
    objects = Mods.objects.all().order_by('creator')
    return render(request, template_name='list2.html',context={'mods': objects} )
