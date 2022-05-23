from re import search
from django.shortcuts import render, redirect
from app.game_form import GamesForm
from app.models import Games
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


def index(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Games.objects.filter(nome__icontains=search)
    else:
        data
    data['db'] = Games.objects.all()
    return render(request, 'login.html', data)


def games(request):
    return render(request, 'games.html')

def form_game(request):
    data = {}
    data['form_game'] = GamesForm()
    return render(request, 'form_game.html', data)

def create(request):
    form_game = GamesForm(request.POST or None)
    if form_game.is_valid():
        form_game.save()
        return render(request, 'index.html')

def view(request, pk):
    data = {}
    data['db'] = Games.objects.get(pk=pk)
    return render(request, 'view.html',data)

def edit(request, pk):
    data = {}
    data['db'] = Games.objects.get(pk=pk)
    data['form_game'] = GamesForm(instance=data['db'])
    return render(request, 'form_game.html', data)

def update(request, pk):
    data = {}
    data['db'] = Games.objects.get(pk=pk)
    form_game = GamesForm(request.POST or None, instance=data['db'])
    if form_game.is_valid():
        form_game.save()
        return render(request, 'index.html')

def delete(request,pk):
    db = Games.objects.get(pk=pk)
    db.delete()
    return render(request, 'index.html')

def avaliar(request, pk):
    data = {}
    data['db'] = Games.objects.get(pk=pk)
    data['form_avalia'] = GamesForm(instance=data['db'])
    return render(request, 'form_avalia.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Games.objects.get(pk=pk)
    data['form_game'] = GamesForm(instance=data['db'])
    return render(request, 'form_game.html', data)


