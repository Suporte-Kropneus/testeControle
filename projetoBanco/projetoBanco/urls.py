
from django.urls import path
from banco.views import home
from banco.views import usuarios
from banco.models import Usuario


urlpatterns = [
    # rota, view responsável, nome de referência
    # usuario.com
    path('',home,name='home'),

    #usuario.com/usuarios
    path('usuarios/',usuarios, name='listagem_usuarios')
]
