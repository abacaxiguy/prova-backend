from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=16)
    email = models.EmailField(verbose_name="e-mail")
    vinculo = models.CharField(max_length=20)