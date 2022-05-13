from rest_framework.routers import SimpleRouter

from .views import UserViewSet, UfViewSet, CidadeViewSet, EnderecoViewSet, \
    OcorrenciaViewSet, PessoaViewSet, ContaViewSet

router = SimpleRouter()

router.register('users', UserViewSet)
router.register('ufs', UfViewSet)
router.register('cidades', CidadeViewSet)
router.register('enderecos', EnderecoViewSet)
router.register('ocorrencias', OcorrenciaViewSet)
router.register('pessoas', PessoaViewSet)
router.register('contas', ContaViewSet)

app_name = 'backend'
urlpatterns = router.urls
