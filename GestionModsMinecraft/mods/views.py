from django.shortcuts import render, redirect
from django.http import HttpResponse
from mods.models import Mods, Version
import requests
import json
from bs4 import BeautifulSoup
import time
import re
import sys
from django.db import IntegrityError
from django.forms import ModelForm , Textarea
from django.forms.fields import DateField , ChoiceField ,MultipleChoiceField
from django import forms

MATCH_ALL = r'.*'
URL = "https://www.minecraftmods.com/"




class ModsForm(ModelForm):
    class Meta:
        model = Mods
        fields = ('title', 'description', 'creator', 'version', 'download', 'img')
        widgets = {
            'description': forms.Textarea(attrs={'cols':20, 'rows': 10,
                'placeholder': 'Description'}),
            'name': forms.TextInput(attrs={'placeholder': 'Just Enough Items'})
        }
        labels = {
            "name": "Nom du mods",
            "description": "Description du mods",
    }
    


def task(request):
    # on instancie un formulaire
    form = ModsForm()
    # on teste si on est bien en validation de formulaire (POST)
    if request.method == "POST":
        # Si oui on récupère les données postées
        form = ModsForm(request.POST)
     # on vérifie la validité du formulaire
        if form.is_valid():
            new_contact = form.save()
            #messages.success(request,'Nouveau task '+new_contact.name)
            #return redirect(reverse('detail', args=[new_contact.pk] ))
            context = {'pers': new_contact}
            return render(request,'detail.html', context)
    # Si méthode GET, on présente le formulaire
    context = {'form': form}
    return render(request,'task.html', context)


def detail(request, cid):
    tache = Mods.objects.get(pk=cid)
    return HttpResponse('Nouvelle tache '+tache.title+' '+tache.version)


def edit(request, pers_id):
    # on récupère la personne
    pers = Mods.objects.get(pk=pers_id)
    # on teste si on est bien en validation de formulaire (POST)
    if request.method == "POST":
        # Si oui on récupère les données postées
        form = ModsForm(request.POST, instance=pers)
        # on vérifie la validité du formulaire
        if form.is_valid():
            form.save()
            #messages.success(request, 'Personne '+pers.name+' modifiée!')
            #return redirect(reverse('detail', args=[pers_id] ))
            context = {'pers': pers}
            return redirect('http://localhost:8000/mods/listing/')
    # Si méthode GET, on présente le formulaire
    form = ModsForm(instance=pers)
    context = {'form': form,'pers': pers}
    return render(request,'edite-crispy.html', context)

def delete(request, pers_id):
    pers = Mods.objects.get(pk=pers_id)
    pers.delete()
    #messages.success(request, 'Personne '+pers.name+' supprimée!')
    form = ModsForm()
    context = {'form': form}
    return redirect('http://localhost:8000/mods/listing')

def liste_version(request, version_id):
    pers = Version.objects.get(pk=version_id)
    objects = Mods.objects.all().filter(version=pers.version)
    return render(request, template_name='version_list.html', context={'objects': objects} )

def liste(request):
    objects = Mods.objects.order_by('title').distinct()
    version = Version.objects.distinct()
    return render(request, template_name='list2.html', context={'objects': objects, 'version': version} )


def scrap(request):
    nbPage = 2
    scraping(nbPage)
    return redirect('http://localhost:8000/mods/listing')

def like(string):
    """
    Return a compiled regular expression that matches the given
    string with any prefix and postfix, e.g. if string = "hello",
    the returned regex matches r".*hello.*"
    """
    string_ = string
    if not isinstance(string_, str):
        string_ = str(string_)
    regex = MATCH_ALL + re.escape(string_) + MATCH_ALL
    return re.compile(regex, flags=re.DOTALL)


def find_by_text(soup, text, tag, **kwargs):
    """
    Find the tag in soup that matches all provided kwargs, and contains the
    text.
    If no match is found, return None.
    If more than one match is found, raise ValueError.
    """
    elements = soup.find_all(tag, **kwargs)
    matches = []
    for element in elements:
        if element.find(text=like(text)):
            matches.append(element)
    if len(matches) > 1:
        raise ValueError("Too many matches:\n" + "\n".join(matches))
    elif len(matches) == 0:
        return None
    else:
        return matches[0]

def scraping(nbPage):
    r = requests.get(URL)
    scrapPage(r)
    if nbPage > 1 :      
        for i in range(2,nbPage):
            print("Page"+str(i))
            r2 = requests.get(URL+"page/"+str(i)+"/")
            scrapPage(r2)

def scrapPage(request):
    soup = BeautifulSoup(request.text,"lxml")
    blogRow = soup.find("section", {"class" : 'main-content'})
    childrenArticles = blogRow.findChildren("article")
    
    for child in childrenArticles:
        mod = Mods()
        a = child.find("a", {"class" : 'transition'})
        mod.img = a.img['src']
        h2 = child.find("h2", {"class" : 'post-title'})
        linkPage = h2.a['href']
        mod.title = h2.text
        divdesc = child.find("div", {"class" : 'post-content'})
        mod.description = divdesc.text
        divcreaver = child.find("div", {"class" : 'post-meta'})
        divver = divcreaver.find("span", {"class" : 'version'})
        mod.version = divver.text
        divcrea = divcreaver.find("span", {"class" : 'developer'})
        mod.creator = divcrea.text
        r2 = requests.get(linkPage.replace(' ',''))
        soup2 = BeautifulSoup(r2.text,"lxml")   
        divdownload = find_by_text(soup2, 'Download', 'a')
        if divdownload == None:
            linkDownload =''
        else: 
            linkDownload = divdownload['href']
        mod.download = linkDownload

        vers = Version()
        divcreaver = child.find("div", {"class" : 'post-meta'})
        divver = divcreaver.find("span", {"class" : 'version'})
        vers.version = divver.text
        


        try:
            mod.save()
            vers.save()
        except IntegrityError:
            pass

        