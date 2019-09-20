from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from .models import *


class MarcaForm(ModelForm):
    class Meta:
        model = Marca
        fields = ['nome', 'categoria']


def criar_marca(request, template_name='marca_form.html'):
    form = MarcaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('marca_list')
    return render(request, template_name, {'form': form})


def listar_marca(request, template_name='marca_list.html'):
    query = request.GET.get('busca')
    if query:
        marca = Marca.objects.filter(nome__icontains=query)
    else:
        marca = Marca.objects.all()
    marcas = {'lista': marca}
    return render(request, template_name, marcas)


def editar_marca(request, pk, template_name='marca_form.html'):
    marca = get_object_or_404(Marca, pk = pk)
    form = MarcaForm(request.POST or None, instance=marca)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('marca_list')
        else:
            form = MarcaForm(instance=marca)
    return render(request, template_name, {'form': form})


def deletar_marca(request, pk, template_name="delete_marca.html"):
    marca = Marca.objects.get(pk=pk)
    if request.method == 'POST':
        marca.delete()
        return redirect('marca_list')
    return render(request, template_name, {'marca': marca})
