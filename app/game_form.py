from django.forms import ModelForm
from app.models import Games

# Create the form class.
class GamesForm(ModelForm):
  class Meta:
    model = Games
    fields = ['nome', 'categoria', 'descrição']