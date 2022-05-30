from django.urls import path,include
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('autenticacao/', include('django.contrib.auth.urls')),
    path('auth/login/', views.login, name='login'),
    path('auth/login/sucesso=<int:sucesso>', views.login, name='login_sucesso')
    
]
