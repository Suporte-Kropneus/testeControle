from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=105)
    idade = models.IntegerField()


    def __str__(self):
        return self.id_usuario
