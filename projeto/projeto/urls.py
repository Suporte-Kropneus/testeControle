from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView


from app.views import *

urlpatterns = [
    
   
    path('', TemplateView.as_view(template_name='home.html'),name='home'),
    path('cria_usuario/',cria_usuario, name='cria_usuarios'),
    path('lista_usuario/',lista_usuarios, name='listagem_usuarios'),
    path('deleta_usuario/<int:pk>/',deleta_usuario,name='deleta_usuario'),
    path('listagem_unica/', lista_um, name='listagem_unica'),
    path('homelista/',lista_dois,name='homelista'),
    path('deletauser/<int:pk>/',deleta_usuario2,name='deletauser'),
    path('update/<int:pk>/',update,name='update_user'),
    path('edit/<int:pk>/',edit , name ='edit_User'),
    path('buscar_usuario/',buscar, name='buscar'),
    path('radio/',lista_radio,name='lista_radio'),
    path('filtrar/',radio,name="filtra_radio"),
    path('deleta_varios/',deleta_varios,name="deleta_var"),



    #--------LINKS PARA TELA DE LOGIN-------


    #link do administrator
    path("admin/", admin.site.urls),

    #link padrão django
    path("accounts/", include("django.contrib.auth.urls"))
    
]

