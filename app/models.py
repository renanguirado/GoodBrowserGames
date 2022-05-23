from pyexpat import model
from statistics import mode
from telnetlib import GA
from django.db import models


class Games(models.Model):
    id = models.BigAutoField(max_length=500,primary_key=True)
    nome = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30)
    descrição = models.CharField(max_length=150)


class Avaliacao(models.Model):
    game = models.ForeignKey(Games, on_delete=models.CASCADE)
    comentario = models.CharField(max_length=150)
    nota = models.IntegerField(max_length=3)
