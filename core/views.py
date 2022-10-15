from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import generics
from django_filters import rest_framework as filters

from core.models import Clientes, Produtos, Pedidos, ItemPedidos
from core.Serializers import ClientesSerializer, ClientesCreatEditSerializer, ProdutosSerializer, ProdutosCreatEditSerializer, PedidosSerializer, PedidosSerializer, PedidosEditCreatSerializer, FaturamentoSerializer, LucroSerializer

#--------------------------View de Clientes--------------------------------
class ClientsViewSet(viewsets.ModelViewSet): 
    queryset = Clientes.objects.all()

    def get_serializer_class(self):
        if self.action =='list'  or self.action == 'create':
            return ClientesSerializer

        return ClientesCreatEditSerializer
        
#--------------------------View de Produtos--------------------------------
class ProdutosViewSet(viewsets.ModelViewSet): 
    queryset = Produtos.objects.all()
    
    def get_serializer_class(self):
        if self.action =='list':
            return ProdutosSerializer
        return ProdutosCreatEditSerializer

#--------------------------View de Clientes--------------------------------
class PedidosViewSet(viewsets.ModelViewSet): 
    queryset = Pedidos.objects.all()

    def get_serializer_class(self):
        if self.action =='list' or  self.action == 'retrieve':
            return PedidosSerializer
        return PedidosEditCreatSerializer

#-----------------------View para lista pedidos pelos cliente---------------
class PedidoClienteView(generics.ListAPIView):
    queryset = Pedidos.objects.all()
    serializer_class = PedidosSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('client',)

#---------------------------View para o faturamento---------------------
class FaturamentoView(generics.ListAPIView):
    queryset = ItemPedidos.objects.all()
    serializer_class = FaturamentoSerializer

    def list(self, request):
        pedidos = self.queryset.all()
        fatura = 0
        for pedido in pedidos:
            fatura += pedido.product.price * pedido.quantity

        total = {'total':fatura}
        serializer = FaturamentoSerializer(total)
        return Response(serializer.data)

#---------------------------View para o lucro---------------------
class LucroView(generics.ListAPIView):
    queryset = ItemPedidos.objects.all()
    serializer_class = LucroSerializer

    def list(self, request):
        pedidos = self.queryset.all()
        lucro = 0
        for pedido in pedidos:
            lucro += (pedido.product.price - pedido.product.cost) * pedido.quantity

        profit = {'profit':lucro}
        serializer = LucroSerializer(profit)
        return Response(serializer.data)
