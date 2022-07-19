from django.db import models


class Clientes(models.Model):
    name = models.CharField('Nome',max_length=255)
    email = models.EmailField('E-mail',max_length=255)
    fone = models.IntegerField('Fone')
    criado = models.DateField('Criado', auto_now_add=True)
    atualizado = models.DateField('Atualizado', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)


class Produtos(models.Model):
    codigo = models.IntegerField('codigo')
    name = models.CharField('Nome do produto',max_length=255)
    descricao = models.TextField('Descricao',max_length=500)
    preco = models.DecimalField('Preço', max_digits=5, decimal_places=2)
    custo = models.DecimalField('Custo', max_digits=5, decimal_places=2)
    estoque = models.BooleanField('Estoque', default=True)

class Pedidos(models.Model):
    cliente = models.ManyToManyField('Clientes', related_name='clientes')
    produto = models.ManyToManyField('Produtos', related_name='produtos')
    quantidade = models.IntegerField('Quantidade')
    total = models.DecimalField('Total', max_digits=5, decimal_places=2,default=0)


