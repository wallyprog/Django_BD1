from django.urls import path,include
from .views import *
from django.conf.urls import url

urlpatterns = [
    path('marca_form',criar_marca, name='criar_marca'),
    path('marca_listar', listar_marca,name='marca_list'),
    path('marca_deletar//(?P<pk>[0-9]+)', deletar_marca, name = 'deletar_marca'),
    path('marca_editar//(?P<pk>[0-9]+',editar_marca,name = 'editar_marca'),
]

