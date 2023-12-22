from django.contrib import admin
from django.urls import path
from app.views import home, lista_usuarios

urlpatterns = [
    path('',home,name='home'),
    path('usuarios/',lista_usuarios, name='listagem_usuarios')
]
