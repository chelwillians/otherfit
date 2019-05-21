from django.db import models

# Create your models here.
class Costumer (models.Model):
    tipo_costumer = [
        ('empresa', 'Empresa'),
        ('pessoa', 'Pessoa')
    ]

    nome_empresa = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    telefones = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null =True) # blank = true aceita vazio assim como null = true
    tipo = models.TextField(choices=tipo_costumer, default='Empresa') 

    def __str__(self):
        return self.nome_empresa # Puxar o nome certinho no admin e o nome não fica "Produto object (1)"

class Client (models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    telefones = models.CharField(max_length=100)
    cpf = models.CharField(max_length=100)

    def __str__(self):
        return self.nome # Puxar o nome certinho no admin e o nome não fica "Produto object (1)"