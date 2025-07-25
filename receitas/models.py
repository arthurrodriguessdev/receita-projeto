from django.db import models
from datetime import datetime

class Receita(models.Model): #Sempre que for fazer a criação de uma model, ela precisa receber como herança essa classe models.Model
    nome_receita = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    data_receita = models.DateTimeField(default=datetime.now, blank=True)

    
