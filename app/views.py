from re import search
import string
from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.game_form import GamesForm, AvalForm
from app.models import Games, Avaliacoes
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'login.html')


def games(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Games.objects.filter(nome__icontains=search)
    else:
        data
    data['db'] = Games.objects.all()
    return render(request, 'index.html', data)

def buscagame(request):
    data = {}
    if request.method == "POST":
        game_buscado = request.POST['search']
        print(game_buscado)
        data['db'] = Games.objects.filter(nome__icontains=game_buscado)
        return render(request, 'index.html',data)
    else:
        return render(request, 'index.html')

def buscagameAdmin(request):
    data = {}
    if request.method == "POST":
        game_buscado = request.POST['search']
        print(game_buscado)
        data['db'] = Games.objects.filter(nome__icontains=game_buscado)
        return render(request, 'admin.html',data)
    else:
        return render(request, 'admin.html')


def gamesadmin(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Games.objects.filter(nome__icontains=search)
    else:
        data
    data['db'] = Games.objects.all()
    return render(request, 'admin.html', data)

def form_game(request):
    data = {}
    data['form_game'] = GamesForm()
    return render(request, 'form_game.html', data)

def create(request):
    form_game = GamesForm(request.POST or None)
    print(form_game)
    if form_game.is_valid():
        form_game.save()
        return redirect('/gamesadmin')

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
        return redirect('/gamesadmin')

def delete(request,pk):
    db = Games.objects.get(pk=pk)
    db.delete()
    return redirect('/gamesadmin')

def avaliar_form(request, pk):
    data = {}
    data['db'] = Games.objects.get(pk=pk)
    data['av'] = Avaliacoes.objects.filter(game_id=pk)
    return render(request, 'avaliar.html', data)

def avaliar(request, pk):
    form_aval = AvalForm(request.POST or None)
    pk_str = str(pk)
    rota = "/avaliar/" + pk_str
    print(rota)
    if form_aval.is_valid():
        form_aval.save()
        return redirect(rota)

def deleteaval(request,pk):
    db = Avaliacoes.objects.get(pk=pk)
    db.delete()
    pk_str = str(db.game_id)
    rota = "/avaliar/" + pk_str
    return redirect(rota)
