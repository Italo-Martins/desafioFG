from rest_framework import serializers

from rest_framework.serializers import SerializerMethodField, CharField

from core.models import Clientes, Produtos, Pedidos, ItemPedidos


#-------------Serializer para cisualizar Cliente----------------
class ClientesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clientes
        fields = ('name', 'email', 'fone')

#-------------Serializer para criar e editar Cliente----------------
class ClientesCreatEditSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clientes
        fields = ('name', 'email', 'fone', 'active')


#-------------Serializer para visualizar Produto--------------------
class ProdutosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produtos
        fields = ('name','description','price', 'quantity')

#-------------Serializer para criar e editar Produto----------------
class ProdutosCreatEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produtos
        fields = '__all__'


#-------------Serializer para mostrar o itens do pedido--------------
class ItensPedidosSerializer(serializers.ModelSerializer):
    
    total = SerializerMethodField()

    class Meta:
        model = ItemPedidos
        fields = ('product', 'quantity', 'total')

    def get_total(self, instace):
        return instace.quantity * instace.product.price

#-------------Serializer para editar o itens do pedido--------------
class ItensCreatEdiSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemPedidos
        fields = ('product', 'quantity')

#-------------Serializer para mostrar pedido--------------
class PedidosSerializer(serializers.ModelSerializer):
    client = CharField(source="client.name")
    order = ItensPedidosSerializer(many=True)
    total = SerializerMethodField()

    class Meta:
        model = Pedidos
        fields = ('client', 'order', 'total')

    def get_total(self, instace):
        total = 0
        pedidos = instace.order.get_queryset()
        for pedido in pedidos:
            total = total + pedido.product.price * pedido.quantity
        return total

#-------------Serializer para editar ou criar pedido--------------
class PedidosEditCreatSerializer(serializers.ModelSerializer):
    order = ItensCreatEdiSerializer(many=True)

    class Meta:
        model = Pedidos
        fields = ('client', 'order')

    def create(self, validated_data):
        orders = validated_data.pop('order')
        pedido = Pedidos.objects.create(**validated_data)
        for order in orders:
            ItemPedidos.objects.create(order=pedido, **order)
        pedido.save()
        return pedido

    def update(self, instace, validated_data):
        orders = validated_data.pop('order')
        if orders:
            instace.order.all().delete()
            for order in orders:
                ItemPedidos.objects.create(order=instace, **order)
            instace.save()
            return instace


#-------------Serializer para mostrar o faturamento total --------------
class FaturamentoSerializer(serializers.Serializer):
    total = serializers.DecimalField(max_digits=12, decimal_places=2)
    
#-------------Serializer para mostrar o lucro total--------------
class LucroSerializer(serializers.Serializer):
    profit = serializers.DecimalField(max_digits=12, decimal_places=2)

