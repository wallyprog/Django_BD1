from django.shortcuts import render,redirect,get_list_or_404
from django.forms import ModelForm
from .models import *

class MarcaForm(ModelForm):
    class Meta:
        model = Marca
        fields=['nome','categoria']


def criar_marca(request, template_name='marca_form.html'):
    form = MarcaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('criar_marca')
    return render(request, template_name,{'form':form})




