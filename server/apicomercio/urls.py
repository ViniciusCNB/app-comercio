from django.urls import path, include
from rest_framework.routers import DefaultRouter
from comercio.views import ProdutoViewSet, ClienteViewSet, CarrinhoViewSet

# É em urls.py que definimos as urls da nossa aplicação

router = DefaultRouter()
router.register('produto', ProdutoViewSet)
router.register('cliente', ClienteViewSet)
router.register('carrinho', CarrinhoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('carrinho/<int:pk>/detalhes', CarrinhoViewSet.as_view({'get': 'get_cliente_e_produto'}), name='carrinho-detalhes') # Rota para o método que retorna os nomes de cliente e produto dado um carrinho
]
