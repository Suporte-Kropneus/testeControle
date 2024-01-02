from django.contrib import admin
from django.urls import path
from app.views import home, edit,lista_usuarios,cria_usuario,deleta_usuario,lista_um,lista_dois,deleta_usuario2,update,buscar

urlpatterns = [
    path('',home,name='home'),
    path('cria_usuario/',cria_usuario, name='cria_usuarios'),
    path('lista_usuario/',lista_usuarios, name='listagem_usuarios'),
    path('deleta_usuario/<int:pk>/',deleta_usuario,name='deleta_usuario'),
    path('listagem_unica/', lista_um, name='listagem_unica'),
    path('homelista/',lista_dois,name='homelista'),
    path('deletauser/<int:pk>/',deleta_usuario2,name='deletauser'),
    path('update/<int:pk>/',update,name='update_user'),
    path('edit/<int:pk>/',edit , name ='edit_User'),
    path('buscar_usuario/',buscar, name='buscar')
]

