from xml.dom import UserDataHandler
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required

def cadastro(request):
    if request.method =='GET':
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('Nome de usuário já existente na plataforma')

        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()


        return HttpResponse('Usuário cadastrado com sucesso!')

    

def login(request):
    if request.method == 'GET':
        return render(request, '/auth/login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user= authenticate (username=username, password=senha)
        
        if user.is_superuser:
            login_django(request, user)
            return redirect('/gamesadmin')
        elif user:
            login_django(request,user)
            return redirect('/games')
        else:
            return HttpResponse('Usuário ou senha inválido')
        