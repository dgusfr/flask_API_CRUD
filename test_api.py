import requests

URL = "http://127.0.0.1:5000/products"

def list_products():
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
    # Dados a serem atualizados, ignorando campos não fornecidos
    payload = {key: value for key, value in {
        "name": name,
        "description": description,
        "price": price,
        "stock": stock
    }.items() if value is not None}

    response = requests.put(f"{URL}/{product_id}", json=payload)
    if response.status_code == 200:
        print("Produto atualizado com sucesso:", response.json())
    else:
        print("Erro ao atualizar produto:", response.status_code, response.text)

def create_product(name, description, price, stock):
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