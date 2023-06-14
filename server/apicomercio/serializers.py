from rest_framework.serializers import ModelSerializer, SerializerMethodField
from comercio.models import Produto, Cliente, Carrinho

# Os serializers ajudam a converter os tipos complexos ou instâncias de modelo em tipos de dados Python nativos que podem ser facilmente renderizados em JSON ou XML ou outros tipos de conteúdo. Eles também fazem o caminho inverso.

class ProdutoSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = ('id_produto', 'nome_produto', 'valor_unit_produto', 'marca_produto')

class ClienteSerializer(ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('cpf_cliente', 'nome_cliente', 'data_nasc_cliente')

class CarrinhoSerializer(ModelSerializer):
    valor_total_carrinho = SerializerMethodField()

    def get_valor_total_carrinho(self, obj): # Retorna o valor do campo diretamente
        return obj.valor_total_carrinho

    class Meta:
        model = Carrinho
        fields = ('id_carrinho', 'cpf_cliente', 'id_produto', 'qntd_produto', 'valor_total_carrinho')