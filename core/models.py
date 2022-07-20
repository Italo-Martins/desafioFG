from django.db import models

# Modelo dos Clientes
class Clientes(models.Model):
    name = models.CharField('Nome',max_length=255) #Nome do cliente
    email = models.EmailField('E-mail',max_length=255) #E-mail do cliente
    fone = models.IntegerField('Fone') #Telefone do cliente
    criado = models.DateField('Criado', auto_now_add=True) #Data de criação
    atualizado = models.DateField('Atualizado', auto_now=True) #Data de modificação
    ativo = models.BooleanField('Ativo?', default=True) #Se o cliente esta ativo ou não


#Modelo dos produtos
class Produtos(models.Model):
    codigo = models.IntegerField('codigo') #Codigo do produto
    name = models.CharField('Nome do produto',max_length=255) #Nome do produto
    descricao = models.TextField('Descricao',max_length=500) #Descrição do produto
    preco = models.DecimalField('Preço', max_digits=5, decimal_places=2) #Preço do produto
    custo = models.DecimalField('Custo', max_digits=5, decimal_places=2) #Custo de produção do produto
    estoque = models.BooleanField('Estoque', default=True) # Se esta em estoque ou não

#Modelo dos pedidos
class Pedidos(models.Model):
    cliente = models.ManyToManyField('Clientes', related_name='clientes') #Cliente que compra
    produto = models.ManyToManyField('Produtos', related_name='produtos') #Produto comprado
    quantidade = models.IntegerField('Quantidade') #Quantidade Comprada
    total = models.DecimalField('Total', max_digits=5, decimal_places=2,default=0) #Valor total do pedido


