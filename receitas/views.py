from django.shortcuts import render
from django.http import HttpResponse

def index(request): #Cria um dicionário receitas com chaves e valores
    receitas = {
        1:'Bolo de cenoura',
        2:'Bolo de chocolate',
        3:'Sorvete de Baunilha',
        4:'Caldo de Frango',
        5:'kakak'
    }

    dados = { #Cria um contexto (dicionário com uma chave recebendo outro dicionário como valor)
        'nome_receita': receitas
    }

    return render(request, 'index.html', dados)

def receita(request):
    return render(request, 'receita.html')