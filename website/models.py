from django.db import models

# Create your models here.
class Costumer (models.Model):
    nome_empresa = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    telefones = models.CharField(max_length=100)
    cpnj = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null =True) # blank = true aceita vazio assim como null = true

    def __str__(self):
        return self.nome_empresa # Puxar o nome certinho no admin e o nome não fica "Produto object (1)"