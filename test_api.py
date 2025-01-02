import requests

URL = "http://127.0.0.1:5000/products"

def list_products():
    response = requests.get(BASE_URL)
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


def create_product(name, description, price, stock):
    payload = {
        "name": name,
        "description": description,
        "price": price,
        "stock": stock
    }
    response = requests.post(BASE_URL, json=payload)
    if response.status_code == 201:
        print("Produto criado com sucesso:", response.json())
    else:
        print("Erro ao criar produto:", response.status_code, response.text)