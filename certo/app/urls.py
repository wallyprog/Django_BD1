from django.urls import path,include
from .views import *
from django.conf.urls import url

urlpatterns = [
    path('marca_form',criar_marca, name='criar_marca'),
]

