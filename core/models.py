from django.db import models

#--------------------------------Modelo dos Clientes----------------------------
class Clientes(models.Model):
    name = models.CharField('Nome',max_length=255) #Nome do cliente
    email = models.EmailField('E-mail',max_length=255, null=True) #E-mail do cliente
    fone = models.IntegerField('Fone') #Telefone do cliente
    created = models.DateField('Criado', auto_now_add=True) #Data de criação
    updated = models.DateField('Atualizado', auto_now=True) #Data de modificação
    active = models.BooleanField('Ativo?', default=True) #Se o cliente esta ativo ou não

#--------------------------------Modelo dos produtos----------------------------
class Produtos(models.Model):
    name = models.CharField('Nome do Produto',max_length=255) #Nome do produto
    description = models.TextField('Descriçao',max_length=500) #Descrição do produto
    price = models.DecimalField('Preço', max_digits=10, decimal_places=2, default=0) #Preço do produto
    cost = models.DecimalField('Custo', max_digits=10, decimal_places=2, default=0) #Custo de produção do produto
    quantity = models.IntegerField('Quantidade em Estoque', default=0) #Quantidade do produto em estoque
    inventory = models.BooleanField('Estoque', default=True) # Se esta em estoque ou não


#--------------------------------Modelo dos pedidos-----------------------------
class Pedidos(models.Model):
    client = models.ForeignKey(Clientes, on_delete=models.PROTECT, related_name='client') #Cliente que comprou

#--------------------------------Modelo dos itens do pedidos--------------------
class ItemPedidos(models.Model):
    order = models.ForeignKey(Pedidos, on_delete=models.CASCADE, related_name='order') #Relaciona com o pedido
    product = models.ForeignKey(Produtos,on_delete=models.PROTECT, related_name='+') #Produto comprado
    quantity = models.IntegerField('Quantidade', default=0) #Quantidade Comprada
