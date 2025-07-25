from django.contrib import admin
from . models import Receita #Importando as models criadas

#Registrando nossa model no admin
admin.site.register(Receita)
