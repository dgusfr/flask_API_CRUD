# CRUD API com Flask e Banco de Dados JSON

Este projeto implementa uma API básica de CRUD (Create, Read, Update, Delete) utilizando Flask como framework backend e um arquivo JSON como banco de dados temporário.

## Estrutura do Projeto


## Dependências

Antes de iniciar, certifique-se de que o Python está instalado. As dependências do projeto estão listadas no arquivo `requirements.txt`. As principais são:

- **Flask**: Framework web utilizado para criar a API.

Endpoints da API
1. Listar Todos os Itens
URL: /items
Método: GET
Resposta:
json
Copiar código
{
  "items": [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"}
  ]
}
2. Criar Novo Item
URL: /items
Método: POST
Corpo da Requisição:
json
Copiar código
{
  "name": "Novo Item"
}
Resposta:
json
Copiar código
{
  "id": 3,
  "name": "Novo Item"
}
3. Atualizar um Item
URL: /items/<id>
Método: PUT
Corpo da Requisição:
json
Copiar código
{
  "name": "Item Atualizado"
}
Resposta:
json
Copiar código
{
  "id": 1,
  "name": "Item Atualizado"
}
4. Deletar um Item
URL: /items/<id>
Método: DELETE
Resposta:
json
Copiar código
{
  "message": "Item deleted"
}
Testes
Os testes estão localizados no diretório tests. Para executá-los, use o seguinte comando:

bash
Copiar código
python -m unittest discover -s tests
Melhorias Futuras
Adicionar suporte a autenticação usando JWT.
Substituir o banco de dados JSON por um banco de dados relacional (SQLite, MySQL, etc.).
Implementar paginação nas listagens de itens.
Documentar a API usando Swagger ou outra ferramenta.