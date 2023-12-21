
from django.urls import path
from banco.views import home
from banco.models import Usuarios


urlpatterns = [
    # rota, view responsável, nome de referência
    # usuario.com
    path('',home,name='home'),

    #usuario.com/usuarios
    path('usuarios/',Usuarios, name='listagem_usuarios')
]
