from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Empresa(models.Model):
    nome = models.CharField(max_length=50)
    empresa = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nome
    
class Rede(models.Model):
    nome = models.CharField(max_length=50)
    vpn = models.CharField(max_length=15)
    end_mac = models.CharField(max_length=15)
    ip = models.CharField(max_length=15)

    def __str__(self):
        return self.nome


class Contas(models.Model):
    nome = models.CharField(max_length=50)

    nome_plat=models.CharField(max_length=30)
    usuario=models.CharField(max_length=50)
    senha=models.CharField(max_length=20)
    senha_extra=models.CharField(max_length=20)
    observacao=models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Usuario(models.Models):
    nome = models.CharField(max_length=50)
    codigo_vendedor = models.IntegerField
    tipo_redirecionamento = models.CharField(max_length=5)
    empresa =models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
