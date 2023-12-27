from django.shortcuts import render
from .models import Usuario
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404


def home(request):
    return render(request,'home.html')
# Create your views here.

def lista_usuarios(request):
    #Exibir todos os usuarios já cadastrados em uma nova pagina
    usuario = {
        'usuarios': Usuario.objects.all()
    }
    #Retornar os dados para a página de listagem de usuários
    return render (request,'usuarios.html',usuario)

def cria_usuario(request):
    
        #SALVAR OS DADOS DA TELA PARA O BANCO
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()

    return redirect('/lista_usuario/')


def deleta_usuario(request,pk):
    data = get_object_or_404(Usuario,pk=pk)
    data.delete()
    return redirect('/lista_usuario/')



def lista_um(request):


    pk = request.GET.get('id')
    usuario_cadastrado =    {
        'usuarios':Usuario.objects.get(id_usuario=pk)    
        }
    
    return render(request,'id_usuario.html',usuario_cadastrado)

def lista_dois(request):


    pk = request.GET.get('id')
    usuario_cadastrado =    {
        'usuarios':Usuario.objects.get(id_usuario=pk)    
        }
    
    return render(request,'home.html',usuario_cadastrado)


def deleta_usuario2(request,pk):
    data = get_object_or_404(Usuario,pk=pk)
    data.delete()

    return redirect('/')

def update(request,pk):

    data = Usuario.objects.get(pk=pk)
    return render(request,'update.html',{'data':data})






