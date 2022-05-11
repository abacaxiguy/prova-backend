from pyexpat import model
from django.db import models
from django.forms import CharField

from django.contrib.auth.models import User

class Conta(models.Model):
    tp_conta = models.CharField(max_length=30)
    id_banco = models.IntegerField()
    banco = models.CharField(max_length=50)
    conta = models.IntegerField()
    agencia = models.IntegerField()
    operacao = models.IntegerField()


class Uf(models.Model):
    nome = models.CharField(max_length=30)
    sigla = models.CharField(max_length=2)


class Cidade(models.Model):
    nome = models.CharField(max_length=50)
    id_uf = models.ForeignKey(Uf, on_delete=models.PROTECT)



class Endereco(models.Model):
    logradouro = models.CharField(max_length=150)
    numero = models.CharField(max_length=8)
    cep = models.CharField(max_length=10)
    bairro = models.CharField(max_length=80)
    complemento = models.CharField(max_length=60)
    observacoes = models.TextField()
    id_cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)



class Pessoa(models.Model):
    vinculo = models.CharField(max_length=20)
    cpf = models.IntegerField()
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=16)
    email = models.EmailField()
    id_user = models.OneToOneField(User)

