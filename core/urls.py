from django.urls import path


from core.views import ClientsCreatView, ClientEdit, ProdutosCreatView, ProdutoEdit, PedidosCreatView, PedidoEdit,ListaPedidos,Fatura, Lucro

#Rotas da aplicação
urlpatterns = [
    path('clientes/', ClientsCreatView.as_view()),
    path('clientes/<int:pk>/', ClientEdit.as_view()),
    path('produtos/', ProdutosCreatView.as_view()),
    path('produtos/<int:pk>/', ProdutoEdit.as_view()),
    path('pedidos/', PedidosCreatView.as_view()),
    path('pedidos/<int:pk>/', PedidoEdit.as_view()),
    path('listapedidos/<int:pk>/', ListaPedidos.as_view()),
    path('fatura/', Fatura.as_view()),
    path('lucro/', Lucro.as_view()),
]