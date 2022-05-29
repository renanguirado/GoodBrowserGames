from django.db import models

class Games(models.Model):
    id = models.BigAutoField(max_length=500,primary_key=True)
    nome = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30)
    descrição = models.CharField(max_length=150)

class Avaliacoes(models.Model):
    id = models.BigAutoField(max_length=500,primary_key=True)
    game_id = models.BigIntegerField(max_length=500)
    autor = models.CharField(max_length=30)
    comentario = models.CharField(max_length=200)
    nota = models.BigIntegerField(max_length=500)
