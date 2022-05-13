from rest_framework import serializers
from backend.models import Uf, Cidade, Endereco, Ocorrencia, Pessoa, Conta
from django.contrib.auth.models import User


class UfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uf
        fields = '__all__'


class CidadeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cidade
        fields = '__all__'

    def to_representation(self, instance):
        ret = super(CidadeSerializer, self).to_representation(instance)

        ret['UF'] = UfSerializer(instance.id_uf).data

        return ret


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'

    def to_representation(self, instance):
        ret = super(EnderecoSerializer, self).to_representation(instance)

        ret['Cidade'] = CidadeSerializer(instance.id_cidade).data

        return ret


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']


class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = '__all__'

    def to_representation(self, instance):
        ret = super(PessoaSerializer, self).to_representation(instance)

        ret['Usuário'] = UserSerializer(instance.id_user).data
        ret['Conta'] = ContaSerializer(instance.id_conta).data
        ret['Endereço'] = EnderecoSerializer(instance.id_endereco).data

        return ret


class OcorrenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ocorrencia
        fields = '__all__'

    def to_representation(self, instance):
        ret = super(OcorrenciaSerializer, self).to_representation(instance)

        ret['Pessoa'] = PessoaSerializer(instance.id_pessoa).data

        return ret


class ContaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conta
        fields = '__all__'
