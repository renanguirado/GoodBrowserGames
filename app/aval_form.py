from dataclasses import field
from pyexpat import model
from django import forms
from app.models import Avaliacao

class AvalForm(forms.ModelForm):
    class Meta:
            model = Avaliacao
            fields = ['comentario','nota']
