from rest_framework import response
from rest_framework.viewsets import ModelViewSet
from django.db.models import ProtectedError
from django.contrib.auth.models import User
from rest_framework.status import HTTP_400_BAD_REQUEST

from .models import Uf, Cidade, Endereco, Conta, Ocorrencia, Pessoa

from .serializers import UserSerializer, UfSerializer, CidadeSerializer, \
    EnderecoSerializer, ContaSerializer, OcorrenciaSerializer, PessoaSerializer


class ExceptDeleteProtectedMixin:
    """
    Handles the ProtectedError from any view
    """

    def destroy(self, req, *args, **kwargs):
        errors = {
            "errors":
            ["Cannot delete this instance because it has been used elsewhere."]
        }

        try:
            return super().destroy(req, *args, **kwargs)
        except ProtectedError:
            return response.Response(errors, HTTP_400_BAD_REQUEST)


class UserViewSet(ExceptDeleteProtectedMixin, ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UfViewSet(ExceptDeleteProtectedMixin, ModelViewSet):
    queryset = Uf.objects.all()
    serializer_class = UfSerializer


class CidadeViewSet(ExceptDeleteProtectedMixin, ModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer


class EnderecoViewSet(ExceptDeleteProtectedMixin, ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer


class ContaViewSet(ExceptDeleteProtectedMixin, ModelViewSet):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer


class OcorrenciaViewSet(ExceptDeleteProtectedMixin, ModelViewSet):
    queryset = Ocorrencia.objects.all()
    serializer_class = OcorrenciaSerializer


class PessoaViewSet(ExceptDeleteProtectedMixin, ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
