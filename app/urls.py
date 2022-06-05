from django.urls import path

from.views import buscagameAdmin, index,games,form_game,create, mais_util,view,edit,update,delete,avaliar_form,avaliar,deleteaval,gamesadmin,buscagame,buscagameAdmin,marcaUtil,mais_util

urlpatterns = [
    path('', index, name='index'),
    path('games/', games, name='games'),
    path('gamesadmin/', gamesadmin, name='gamesadmin'),
    path('form_game/', form_game, name='formulario'),
    path('create/', create, name='create'),
    path('view/<int:pk>/', view, name='view'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('update/<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('buscar/', buscagame, name='buscar'),
    path('buscaradmin/', buscagameAdmin, name='buscarAdmin'),
    path('avaliar/<int:pk>/', avaliar_form, name='avaliar_form'),
    path('createaval/<int:pk>/', avaliar, name='createaval'),
    path('deleteaval/<int:pk>/', deleteaval, name='deleteaval'),
    path('marcautil/<int:pk>/',marcaUtil, name='marcautil'),
    path('maisutil/<int:pk>/',mais_util, name='mais_util'),
]
