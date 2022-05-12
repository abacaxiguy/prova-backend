from django.db import models
from django.contrib.auth.models import User


class Conta(models.Model):
    id_conta = models.BigAutoField(
        primary_key=True
    )
    tp_conta = models.CharField(
        choices=(
            ("Poupança", "Poupança"),
            ("Corrente", "Corrente"),
        ),
        verbose_name="Tipo da conta",
        max_length=30,
        blank=False,
        null=False
    )
    id_banco = models.IntegerField(
        blank=False,
        null=False
    )
    banco = models.CharField(
        choices=(
            ("Banco 1", "Banco 1"),
            ("Banco 2", "Banco 2"),
            ("Banco 3", "Banco 3"),
            ("Banco 4", "Banco 4"),
        ),
        max_length=50,
        blank=False,
        null=False
    )
    conta = models.IntegerField(
        blank=False,
        null=False
    )
    agencia = models.IntegerField(
        verbose_name="Agência",
        blank=False,
        null=False
    )
    operacao = models.IntegerField(
        verbose_name="Operação",
        blank=False,
        null=False
    )

    class Meta:
        db_table = "contas"

    def __str__(self):
        return f'{self.banco}: {self.agencia}/{self.conta}'


class Uf(models.Model):
    id_uf = models.BigAutoField(primary_key=True)
    nome = models.CharField(
        max_length=30,
        blank=False,
        null=False
    )
    sigla = models.CharField(
        max_length=2,
        blank=False,
        null=False
    )

    class Meta:
        db_table = "ufs"

    def __str__(self):
        return f'{self.name} - {self.sigla}'


class Cidade(models.Model):
    id_cidade = models.BigAutoField(primary_key=True)
    nome = models.CharField(
        max_length=50,
        blank=False,
        null=False
    )
    id_uf = models.ForeignKey(
        Uf,
        on_delete=models.PROTECT,
        blank=False,
        null=False
    )

    class Meta:
        db_table = "cidades"

    def __str__(self):
        return f'{self.nome}/{self.id_uf.sigla}'


class Endereco(models.Model):
    id_endereco = models.BigAutoField(primary_key=True)
    logradouro = models.CharField(
        max_length=150,
        blank=False,
        null=False
    )
    numero = models.CharField(
        verbose_name="Número",
        max_length=8,
        blank=False,
        null=False
    )
    cep = models.CharField(
        verbose_name="CEP",
        max_length=10,
        blank=False,
        null=False
    )
    bairro = models.CharField(
        max_length=80,
        blank=False,
        null=False
    )
    complemento = models.CharField(
        max_length=60,
    )
    observacoes = models.TextField(
        verbose_name="Observações",
    )
    id_cidade = models.ForeignKey(
        Cidade,
        on_delete=models.PROTECT,
        blank=False,
        null=False
    )

    class Meta:
        db_table = "enderecos"
        verbose_name = "Endereço"

    def __str__(self):
        return f'{self.bairro} - {self.cep}'


class Pessoa(models.Model):
    id_pessoa = models.BigAutoField(primary_key=True)
    vinculo = models.CharField(
        max_length=20,
        choices=(
            ("Vinculo 1", "Vinculo 1"),
            ("Vinculo 2", "Vinculo 2"),
        ),
        blank=False,
        null=False
    )
    cpf = models.IntegerField(
        blank=False,
        null=False
    )
    nome = models.CharField(
        max_length=200,
        blank=False,
        null=False
    )
    telefone = models.CharField(
        max_length=16,
        blank=False,
        null=False
    )
    email = models.EmailField(
        verbose_name="E-mail",
        blank=False,
        null=False
    )
    id_user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        blank=False,
        null=False
    )
    id_endereco = models.ForeignKey(
        Endereco,
        on_delete=models.PROTECT,
        blank=False,
        null=False
    )
    id_conta = models.ForeignKey(
        Conta,
        on_delete=models.PROTECT,
        blank=False,
        null=False
    )

    class Meta:
        db_table = "pessoas"

    def __str__(self):
        return self.nome


class Ocorrencia(models.Model):
    id_ocorrencia = models.BigAutoField(primary_key=True)
    data = models.DateField(
        blank=False,
        null=False
    )
    realizada = models.BooleanField(
        blank=False,
        null=False
    )
    ocorrencia = models.TextField(
        verbose_name="Ocorrência",
        blank=False,
        null=False
    )
    id_pessoa = models.ForeignKey(
        Pessoa,
        on_delete=models.PROTECT,
        blank=False,
        null=False
    )

    class Meta:
        verbose_name = "Ocorrência"

    def __str__(self):
        return f'{self.id_ocorrencia} - {self.id_pessoa.nome}'
