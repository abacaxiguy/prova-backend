from django.contrib import admin
# from django.contrib.auth.models import User

from .models import Uf, Cidade, Endereco, Conta, Pessoa, Ocorrencia


@admin.register(Uf)
class UfAdmin(admin.ModelAdmin):
    list_display = ['nome', 'sigla']
    list_display_links = ['nome', 'sigla']


@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ['nome']
    list_display_links = ['nome']


@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ['logradouro', 'numero', 'bairro', 'cep']
    list_display_links = ['logradouro']


@admin.register(Conta)
class ContaAdmin(admin.ModelAdmin):

    def conta_e_agencia(obj):
        return f'{obj.conta}/{obj.agencia}'

    list_display = [conta_e_agencia, 'tp_conta', 'banco']
    list_display_links = [conta_e_agencia, 'tp_conta', 'banco']


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cpf', 'telefone', 'vinculo']
    list_display_links = ['nome', 'cpf', 'telefone', 'vinculo']


@admin.register(Ocorrencia)
class OcorrenciaAdmin(admin.ModelAdmin):

    list_display = ['id_ocorrencia', 'data', 'realizada']
    list_display_links = ['id_ocorrencia', 'data']
    list_editable = ['realizada']
