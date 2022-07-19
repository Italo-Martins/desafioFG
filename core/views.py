from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets

from core.models import Clientes, Produtos, Pedidos
from core.Serializers import ClientesSerializer, ProdutosSerializer, PedidosSerializer, ListaPedidosSerializer

# class ClientesViewSet(viewsets.ModelViewSet):
#     queryset = Clientes.objects.all()
#     serializer_class = ClientesSerializer

# class ProdutosViewSet(viewsets.ModelViewSet):
#     queryset = Produtos.objects.all()
#     serializer_class = ProdutosSerializer

# class PedidosViewSet(viewsets.ModelViewSet):
#     queryset = Pedidos.objects.all()
#     serializer_class = PedidosSerializer




#View para vizualizar e criar clientes
class ClientsCreatView(APIView):
    def get(self, request):
        todos_clientes = Clientes.objects.all()
        serializer = ClientesSerializer(todos_clientes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClientesSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

#View para editar clientes
class ClientEdit(APIView):
    def get_client(self, pk):
        try:
            client = Clientes.objects.get(pk=pk)
            return client
        except Clientes.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        client = self.get_client(pk)
        serializer = ClientesSerializer(client)
        return Response(serializer.data)

    def put(self, request, pk):
        client = self.get_client(pk)
        serializer = ClientesSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        client = self.get_client(pk)
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#View para vizualizar e criar produtos
class ProdutosCreatView(APIView):
    def get(self, request):
        todos_produtos = Produtos.objects.all()
        serializer = ProdutosSerializer(todos_produtos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProdutosSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#View para editar produtos
class ProdutoEdit(APIView):
    def get_product(self, pk):
        try:
            product = Produtos.objects.get(pk=pk)
            return product
        except Produtos.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        product = self.get_product(pk)
        serializer = ProdutosSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        product = self.get_product(pk)
        serializer = ProdutosSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_product(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#View para vizualizar e criar pedidos
class PedidosCreatView(APIView):
    def get(self, request):
        todos_produtos = Pedidos.objects.all()
        serializer = PedidosSerializer(todos_produtos, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        quantidade = data.get('quantidade')
        id_produto = data.get('produto')[0]
        preco = Produtos.objects.get(pk=id_produto).preco
        total = preco * quantidade
        #import pdb; pdb.set_trace()
        data['total'] = total
        serializer = PedidosSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#View para editar pedidos
class PedidoEdit(APIView):
    def get_product(self, pk):
        try:
            product = Pedidos.objects.get(pk=pk)
            return product
        except Pedidos.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        product = self.get_product(pk)
        serializer = PedidosSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        product = self.get_product(pk)
        serializer = PedidosSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_product(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ListaPedidos(APIView):

    def get_cliente(self, pk):
        try:
            cliente = Clientes.objects.get(pk=pk)
            produtos = Pedidos.objects.filter(cliente=cliente)
            return produtos
        except Pedidos.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, resquest,pk):
        produtos = self.get_cliente(pk)
        serializer = ListaPedidosSerializer(produtos, many=True)
        return Response(serializer.data)

class Fatura(APIView):

    def get_pedidos(self):
        try:
            pedidos = Pedidos.objects.all()
            return pedidos
        except Pedidos.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, resquest):
        pedidos = self.get_pedidos()

        fatura = 0
        for pedido in pedidos:
            fatura += pedido.total

        #import pdb; pdb.set_trace()
    
        return Response({"Fatura": fatura})
