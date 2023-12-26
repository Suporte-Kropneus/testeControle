from django.contrib import admin
from django.urls import path
from app.views import home, lista_usuarios,cria_usuario,deleta_usuario,lista_um

urlpatterns = [
    path('',home,name='home'),
    path('cria_usuario/',cria_usuario, name='cria_usuarios'),
    path('lista_usuario/',lista_usuarios, name='listagem_usuarios'),
    path('deleta_usuario/<int:pk>/',deleta_usuario,name='deleta_usuario'),
    path('listagem_unica/', lista_um, name='listagem_unica')
    
]

