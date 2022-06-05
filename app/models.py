from ctypes import util
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

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
    util = models.BigIntegerField(max_length=500, default=0)
    liked = models.ManyToManyField(User, default=None, blank=True)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avaliacoes = models.ForeignKey(Avaliacoes, on_delete=models.CASCADE)
    estado = models.CharField(default='Like', max_length=10)
