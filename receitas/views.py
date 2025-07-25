from django.shortcuts import render
from django.http import HttpResponse

def index(request): #Cria um dicionário receitas com chaves e valores
    receitas = {
        1:'Bolo de cenoura',
        2:'Bolo de chocolate',
        3:'Sorvete de Baunilha',
        4:'Caldo de Frango',
        5:'Caldo de Feijão',
        6:'Lasanha de Frango',
    }

    context = {
        'nome_receita': receitas
    }

     #Cria um contexto (dicionário com uma chave recebendo outro dicionário como valor)
     

    return render(request, 'index.html', context)

def receita(request):
    return render(request, 'receita.html')