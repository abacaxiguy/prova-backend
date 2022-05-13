from rest_framework import viewsets

from django.contrib.auth.models import User

from .models import Uf, Cidade, Endereco, Conta, Ocorrencia, Pessoa

from .serializers import UserSerializer, UfSerializer, CidadeSerializer, \
    EnderecoSerializer, ContaSerializer, OcorrenciaSerializer, PessoaSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UfViewSet(viewsets.ModelViewSet):
    queryset = Uf.objects.all()
    serializer_class = UfSerializer


class CidadeViewSet(viewsets.ModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer


class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer


class ContaViewSet(viewsets.ModelViewSet):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer


class OcorrenciaViewSet(viewsets.ModelViewSet):
    queryset = Ocorrencia.objects.all()
    serializer_class = OcorrenciaSerializer


class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
