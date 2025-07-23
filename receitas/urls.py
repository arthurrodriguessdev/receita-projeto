#Módulo urls.py PRECISA ser criado dentro do app
from django.urls import path
from receitas.views import index, receita

urlpatterns = [
    path('', index, name='index'),
    path('receita', receita, name='receita'),
]