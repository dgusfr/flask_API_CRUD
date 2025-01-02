import requests

URL = "http://127.0.0.1:5000/products"

def list_products():
    """
    Lista todos os produtos disponíveis na API.
    """
    response = requests.get(URL)
    if response.status_code == 200:
        products = response.json()
        if not products:
            print("Nenhum produto disponível.")
        else:
            print("Produtos disponíveis:")
            for product in products:
                print(f"- ID: {product['id']}, Nome: {product['name']}, Estoque: {product['stock']}")
    else:
        print("Erro ao listar produtos:", response.status_code, response.text)

def get_product_by_id(product_id):
    """
    Busca um produto específico pelo ID.
    """
    response = requests.get(f"{URL}/{product_id}")
    if response.status_code == 200:
        product = response.json()
        print("Produto encontrado:")
        print(f"ID: {product['id']}, Nome: {product['name']}, Descrição: {product['description']}, Preço: {product['price']}, Estoque: {product['stock']}")
        return product
    else:
        print("Erro ao buscar produto:", response.status_code, response.text)
        return None

def update_product(product_id, name=None, description=None, price=None, stock=None):
    """
    Atualiza os dados de um produto pelo ID.
    """
    data = {
        "name": name,
        "description": description,
        "price": price,
        "stock": stock
    }

    # Filtrar campos com valores válidos
    payload = {}
    for key, value in data.items():
        if value is not None:
            payload[key] = value

    response = requests.put(f"{URL}/{product_id}", json=payload)
    if response.status_code == 200:
        print("Produto atualizado com sucesso:", response.json())
    else:
        print("Erro ao atualizar produto:", response.status_code, response.text)

def create_product(name, description, price, stock):
    """
    Cria um novo produto.
    """
    payload = {
        "name": name,
        "description": description,
        "price": price,
        "stock": stock
    }
    response = requests.post(URL, json=payload)
    if response.status_code == 201:
        print("Produto criado com sucesso:", response.json())
    else:
        print("Erro ao criar produto:", response.status_code, response.text)

def delete_product(product_id):
    """
    Exclui um produto pelo ID.
    """
    response = requests.delete(f"{URL}/{product_id}")
    if response.status_code == 200:
        print("Produto excluído com sucesso.")
    else:
        print("Erro ao excluir produto:", response.status_code, response.text)

if __name__ == "__main__":
    # Testes
    print("=== Listar produtos ===")
    list_products()

    print("\n=== Criar produto ===")
    create_product("Cadeira Gamer", "Cadeira confortável para jogos", 599.99, 10)

    print("\n=== Listar produtos ===")
    list_products()

    print("\n=== Atualizar produto ===")
    update_product(1, name="Cadeira Gamer Premium", price=699.99)

    print("\n=== Listar produtos ===")
    list_products()

    print("\n=== Excluir produto ===")
    delete_product(1)

    print("\n=== Listar produtos ===")
    list_products()
