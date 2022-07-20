from rest_framework import serializers

from core.models import Clientes, Produtos, Pedidos

class ClientesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clientes
        fields = '__all__'


class ProdutosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produtos
        fields = '__all__'


class PedidosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pedidos
        fields = '__all__'

class ListaPedidosSerializer(serializers.ModelSerializer):
    produto = ProdutosSerializer(many=True)

    class Meta:
        model = Pedidos
        fields = ['quantidade', 'total', 'produto']

