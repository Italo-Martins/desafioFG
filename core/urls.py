from django.urls import path
from rest_framework.routers import DefaultRouter


from core.views import ClientsCreatView, ClientEdit, ProdutosCreatView, ProdutoEdit, PedidosCreatView, PedidoEdit,ListaPedidos,Fatura

urlpatterns = [
    path('clientes/', ClientsCreatView.as_view()),
    path('clientes/<int:pk>/', ClientEdit.as_view()),
    path('produtos/', ProdutosCreatView.as_view()),
    path('produtos/<int:pk>/', ProdutoEdit.as_view()),
    path('pedidos/', PedidosCreatView.as_view()),
    path('pedidos/<int:pk>/', PedidoEdit.as_view()),
    path('listapedidos/<int:pk>/', ListaPedidos.as_view()),
    path('fatura/', Fatura.as_view()),
]