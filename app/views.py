from django.shortcuts import render
from app.game_form import GamesForm

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def games(request):
    return render(request, 'games.html')

def form_game(request):
    data = {}
    data['form_game'] = GamesForm()
    return render(request, 'form_game.html', data)