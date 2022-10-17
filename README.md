# Desafio Fábrica de Gênios

- A aplicação desenvolvida consiste em sistema pedidos utilizando Django REST Framework.
- Toda a comunicação se da através de JSON.

### O projeto tem as seguintes rotas:
- admin/
- clientes/
- clientes/<int:pk>/
- produtos/
- produtos/<int:pk>/
- pedidos/
- pedidos/<int:pk>/
- listapedidos/<int:pk>/
- faturamento/
- lucro/

### Para cadastra um cliente, produto ou pedido basta acessar as seguintes rotas respectivamente:
- clientes/
- produtos/
- pedidos/

### Para cadastrar um cliente:
```
{
    "name": "Nome",
    "email": "E-mail",
    "fone": +55864865413
}
```
### Para cadastrar um produto:
```
{
    "codigo": 1355,
    "name": "Nome",
    "descricao": "Descrição do Produto",
    "preco": "decimal",
    "custo": "decimal"
}
```
### Para cadastrar um pedido:
```
{
    "client": "Nome",
    "order": [
        {
            "product": id,
            "quantity": 2,
            "total": decimal
        }
    ],
    "total": decimal
    
```
obs.: produto e clientes referisse ao id deles.

### Para acessar um cliente, produto ou pedido especifico basta informar seu id na URL:
- clientes/<int:pk>/
- produtos/<int:pk>/
- pedidos/<int:pk>/

### Para verificar os produtos adquiridos por algum cliente baste acessar o endpoint informando o id do cliente na URL:
- pedidocliente/<int:pk>/

### Para verificar a fatura e o lucros do sistema basta acessar os seguintes endpoints respectivamente:
- faturamento/
- lucro/