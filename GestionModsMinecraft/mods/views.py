from django.shortcuts import render, redirect
from django.http import HttpResponse
from mods.models import Mods




from django.forms import ModelForm , Textarea
from django.forms.fields import DateField , ChoiceField ,MultipleChoiceField
from django import forms




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
    return redirect('http://localhost:8000/mods/listing/')


def liste(request):
    objects = Mods.objects.all().order_by('title')
    return render(request, template_name='list2.html', context={'objects': objects} )
