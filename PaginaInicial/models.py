from django.db import models

# Create your models here.

class Cadastro(models.Model):
    nome = models.TextField(max_length=50)
    idade = models.IntegerField(blank=True, null=True)
    email = models.TextField(max_length=50)
    ativo = models.CharField(max_length=1)
    dt_cadastro = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
