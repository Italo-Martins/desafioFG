from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.views import ClientsViewSet, ProdutosViewSet, PedidosViewSet,PedidoClienteView, FaturamentoView, LucroView

routers = DefaultRouter()
routers.register(r'clientes', ClientsViewSet)
routers.register(r'produtos', ProdutosViewSet)
routers.register(r'pedidos', PedidosViewSet)

#Rotas da aplicação
urlpatterns = [
    path('pedidocliente/', PedidoClienteView.as_view()),
    path('faturamento/', FaturamentoView.as_view()),
    path('lucro/', LucroView.as_view()),
    path('', include(routers.urls))
]