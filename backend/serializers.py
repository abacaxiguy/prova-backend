from rest_framework import serializers
from backend.models import Pessoa, Ocorrencia, Uf, Cidade, Endereco, Conta
from django.contrib.auth.models import User


class UfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uf
        fields = '__all__'


class CidadeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cidade
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']


class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = '__all__'


class OcorrenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ocorrencia
        fields = '__all__'


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'


class ContaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conta
        fields = '__all__'
