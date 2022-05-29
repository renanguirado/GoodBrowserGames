from django.forms import ModelForm
from app.models import Games, Avaliacoes

# Create the form class.
class GamesForm(ModelForm):
  class Meta:
    model = Games
    fields = ['nome', 'categoria', 'descrição']
  
class AvalForm(ModelForm):
  class Meta:
    model = Avaliacoes
    fields = ['game_id','autor', 'comentario', 'nota']
