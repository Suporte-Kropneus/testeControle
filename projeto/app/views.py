from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request,'home.html')
# Create your views here.

def lista_usuarios(request):

    #SALVAR OS DADOS DA TELA PARA O BANCO
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()

    #Exibir todos os usuarios já cadastrados em uma nova pagina
    usuario = {
        'usuarios': Usuario.objects.all()
    }

    #Retornar os dados para a página de listagem de usuários
    return render (request,'usuarios.html',usuario)
