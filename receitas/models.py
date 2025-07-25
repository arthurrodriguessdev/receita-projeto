from django.db import models
from datetime import datetime #Importado para registrar a hora de criação da receita

class Receita(models.Model): #Sempre que for fazer a criação de uma model, ela precisa receber como herança essa classe models.Model
    nome_receita = models.CharField(max_length=200) #Nome da receita será um campo com no máximo 200 caracteres
    ingredientes = models.TextField() #Ingredientes será um campo maior, sem limite
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField() #Será número inteiro
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    data_receita = models.DateTimeField(default=datetime.now, blank=True) #Utilizamos o módulo datatime para registrar a hora exata

    
