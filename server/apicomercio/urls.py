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
]
