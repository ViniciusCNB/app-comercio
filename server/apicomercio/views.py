from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from apicomercio.models import Produto, Cliente, Carrinho
from apicomercio.serializers import ProdutoSerializer, ClienteSerializer, CarrinhoSerializer

# É em views.py que ficam os serviços da aplicação

# Endpoints para os métodos GET, PUT, POST e DELETE para a tabela Produto:
class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


# Endpoints para os métodos GET, PUT, POST e DELETE para a tabela Cliente:
class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


# Endpoints para os métodos GET, PUT, POST e DELETE para a tabela Carrinho:
class CarrinhoViewSet(ModelViewSet):
    queryset = Carrinho.objects.all()
    serializer_class = CarrinhoSerializer

    # Função para calcular o valor total e atribuí-lo ao campo valor_total_carrinho durante a criação de um carrinho. O método perform_create é responsável por calcular o valor total do carrinho com base no produto selecionado e na quantidade, e em seguida, atribuí-lo ao campo valor_total_carrinho antes de salvar o carrinho no banco de dados.
    def perform_create(self, serializer):
        valor_unit_produto = serializer.validated_data['id_produto'].valor_unit_produto
        qntd_produto = serializer.validated_data['qntd_produto']
        valor_total_carrinho = valor_unit_produto * qntd_produto
        serializer.save(valor_total_carrinho = valor_total_carrinho)

    # Método para retornar o nome do cliente e o nome do produto, dado um ID de carrinho
    def get_cliente_e_produto(self, request, *args, **kwargs):
        # OBS: *args e **kwargs -> usados para passar um número variável de argumentos para uma função
        carrinho_id = self.kwargs.get('pk')

        try:
            carrinho = Carrinho.objects.get(pk = carrinho_id)
            nome_cliente = carrinho.cpf_cliente.nome_cliente
            nome_produto = carrinho.id_produto.nome_produto
            response_data = {
                'nome_cliente': nome_cliente,
                'nome_produto': nome_produto,
            }
            return Response(response_data)
        except Carrinho.DoesNotExist:
            return Response({'message': 'Carrinho não encontrado.'})