# CRUD API com Flask e Banco de Dados JSON

Este projeto implementa uma API básica de CRUD (Create, Read, Update, Delete) utilizando Flask como framework backend e um arquivo JSON como banco de dados temporário.

## Tecnologias Utilizadas

<div style="display: flex; flex-direction: row;">
  <div style="margin-right: 20px; display: flex; justify-content: flex-start;">
    <img src="images/pyhton.png" alt="Logo Linguagem" width="100"/>
  </div>
  <div style="margin-right: 20px; display: flex; justify-content: flex-start;">
    <img src="images/flask.png" alt="Logo Linguagem" width="100"/>
  </div>
</div>


## Estrutura do Projeto

```
crud_flask/
├── app.py                    # Arquivo principal para inicialização da aplicação
├── database.json             # Arquivo JSON usado como banco de dados temporário
├── routes/                   # Diretório com as definições de rotas
│   ├── __init__.py           # Inicializador do módulo de rotas
│   ├── item_routes.py        # Rotas relacionadas aos itens
├── controllers/              # Diretório com os controladores
│   ├── __init__.py           # Inicializador do módulo de controladores
│   ├── item_controller.py    # Controlador para operações de CRUD
├── services/                 # Diretório com serviços auxiliares
│   ├── __init__.py           # Inicializador do módulo de serviços
│   ├── json_service.py       # Serviço para manipulação do arquivo JSON
├── utils/                    # Diretório com utilitários
│   ├── __init__.py           # Inicializador do módulo de utilitários
│   ├── validators.py         # Validações para entradas de dados
├── tests/                    # Diretório para testes
│   ├── __init__.py           # Inicializador do módulo de testes
│   ├── test_items.py         # Testes para a API de itens
├── requirements.txt          # Dependências do projeto
├── .gitignore                # Arquivo para ignorar arquivos/diretórios no Git
└── README.md                 # Documentação do projeto
```

## Dependências

Antes de iniciar, certifique-se de que o Python está instalado. As dependências do projeto estão listadas no arquivo `requirements.txt`. As principais são:

- **Flask**: Framework web utilizado para criar a API.

## Endpoints da API

1. **Listar Todos os Itens**  
   **URL:** `/items`  
   **Método:** `GET`  
   **Resposta:**  
   ```json
   {
     "items": [
       {"id": 1, "name": "Item 1"},
       {"id": 2, "name": "Item 2"}
     ]
   }
   ```

2. **Criar Novo Item**  
   **URL:** `/items`  
   **Método:** `POST`  
   **Corpo da Requisição:**  
   ```json
   {
     "name": "Novo Item"
   }
   ```  
   **Resposta:**  
   ```json
   {
     "id": 3,
     "name": "Novo Item"
   }
   ```

3. **Atualizar um Item**  
   **URL:** `/items/<id>`  
   **Método:** `PUT`  
   **Corpo da Requisição:**  
   ```json
   {
     "name": "Item Atualizado"
   }
   ```  
   **Resposta:**  
   ```json
   {
     "id": 1,
     "name": "Item Atualizado"
   }
   ```

4. **Deletar um Item**  
   **URL:** `/items/<id>`  
   **Método:** `DELETE`  
   **Resposta:**  
   ```json
   {
     "message": "Item deleted"
   }
   ```

## Testes

Os testes estão localizados no diretório `tests`. Para executá-los, use o seguinte comando:

```bash
python -m unittest discover -s tests
```

## Melhorias Futuras

- Adicionar suporte a autenticação usando JWT.  
- Substituir o banco de dados JSON por um banco de dados relacional (SQLite, MySQL, etc.).  
- Implementar paginação nas listagens de itens.  
- Documentar a API usando Swagger ou outra ferramenta.

## Autor

Desenvolvido por Diego Franco
