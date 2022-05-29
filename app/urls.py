from django.urls import path

from.views import index,games,form_game,create,view,edit,update,delete,avaliar_form,avaliar

urlpatterns = [
    path('', index, name='index'),
    path('games/', games, name='games'),
    path('form_game/', form_game, name='formulario'),
    path('create/', create, name='create'),
    path('view/<int:pk>/', view, name='view'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('update/<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('avaliar/<int:pk>/', avaliar_form, name='avaliar_form'),
    path('createaval/<int:pk>/', avaliar, name='createaval'),
]
