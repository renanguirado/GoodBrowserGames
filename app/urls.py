from django.urls import path

from.views import index,login,games,form_game

urlpatterns = [
    path('', index),
    path('login', login),
    path('games', games),
    path('form_game', form_game)

]
