from django.shortcuts import render, redirect
from django.http import HttpResponse
from mods.models import Mods
import requests
import json
from bs4 import BeautifulSoup
import time
import re
import sys
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
    return HttpResponse('Nouvelle tache '+tache.name+' '+tache.email)


def edit(request, pers_id):
    # on récupère la personne
    pers = Mods.objects.get(pk=pers_id)
    # on teste si on est bien en validation de formulaire (POST)
    if request.method == "POST":
        # Si oui on rscrapécupère les données postées
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
    return redirect('http://localhost:8000/mods/listing/')


def liste(request):
    objects = Mods.objects.all().order_by('title')
    return render(request, template_name='list2.html', context={'objects': objects} )

def scrap(request):
    scrap(3)
    context = {
        'new_mod_id': mod.pk,
    }
    return render(request,'list2.html', context)

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

def scrap(nbPage):
    r = requests.get(URL)
    scrapPage(r)
    if int(nbPage) > 1 :      
        for i in range(2,nbPage):
            r2 = requests.get(URL+"page/"+str(i)+"/")
            scrapPage(r2)

def scrapPage(request):
    soup = BeautifulSoup(request.text,"lxml")
    #print(soup.prettify())
    blogRow = soup.find("section", {"class" : 'main-content'})
    childrenArticles = blogRow.findChildren("article")
    for child in childrenArticles:
        mod = Mods()
        a = child.find("a", {"class" : 'transition'})
        print('Lien image:')
        print(a.img['src'])
        mod.img = a.img['src']
        h2 = child.find("h2", {"class" : 'post-title'})
        print('Lien page:')
        print(h2.a['href'])
        linkPage = h2.a['href']
        print('Titre:')
        print(h2.text)
        mod.title = h2.text
        divdesc = child.find("div", {"class" : 'post-content'})
        print('Description:')
        print(divdesc.text)
        mod.description = divdesc.text
        divcreaver = child.find("div", {"class" : 'post-meta'})
        divver = divcreaver.find("span", {"class" : 'version'})
        print('Version:')
        print(divver.text)
        mod.version = divver.text
        divcrea = divcreaver.find("span", {"class" : 'developer'})
        print('Creator:')
        print(divcrea.text)
        mod.creator = divcrea.text
        r2 = requests.get(linkPage.replace(' ',''))
        soup2 = BeautifulSoup(r2.text,"lxml")   
        divdownload = find_by_text(soup2, 'Download', 'a')
        if divdownload['href'] != 'Nonetype':
            linkDownload = divdownload['href']
        else: 
            linkDownload =''
        print('Lien download:')
        print(linkDownload)
        mod.download = linkDownload
        mod.save()
        
           