
from django.urls import path
from banco.views import home
from banco.views import lista_usuarios


urlpatterns = [
    # rota, view responsável, nome de referência
    # usuario.com
    path('',home,name='home'),

    #usuario.com/usuarios
    path('usuarios/',lista_usuarios, name='listagem_usuarios')
]
