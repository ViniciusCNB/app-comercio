from django.db.models import AutoField, CharField, Model, FloatField, DateField, ForeignKey, CASCADE, BigIntegerField, IntegerField

# Modelos (tabelas) criados para a aplicação do comércio

class Produto(Model):
		id_produto = AutoField(primary_key=True)
		nome_produto = CharField(max_length=50)
		valor_unit_produto = FloatField()
		marca_produto = CharField(max_length=30)

class Cliente(Model):
		cpf_cliente = BigIntegerField(primary_key=True)
		nome_cliente = CharField(max_length=200)
		data_nasc_cliente = DateField()

class Carrinho(Model):
		id_carrinho = AutoField(primary_key=True)
		cpf_cliente = ForeignKey(Cliente, on_delete=CASCADE)
		id_produto = ForeignKey(Produto, on_delete=CASCADE)
		qntd_produto = IntegerField()
		valor_total_carrinho = FloatField(blank=True, null=True) # Para que possa aceitar valores vazios incialmente
		