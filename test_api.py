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

def main():
    while True:
        print("\nSelecione uma operação:")
        print("1 - Listar produtos")
        print("2 - Buscar produto por ID")
        print("3 - Criar produto")
        print("4 - Atualizar produto")
        print("5 - Excluir produto")
        print("0 - Sair")

        choice = input("Digite sua escolha: ")

        match choice:
            case "1":
                list_products()
            case "2":
                product_id = input("Digite o ID do produto: ")
                get_product_by_id(product_id)
            case "3":
                name = input("Digite o nome do produto: ")
                description = input("Digite a descrição do produto: ")
                price = float(input("Digite o preço do produto: "))
                stock = int(input("Digite o estoque do produto: "))
                create_product(name, description, price, stock)
            case "4":
                product_id = input("Digite o ID do produto: ")
                name = input("Digite o novo nome do produto (ou pressione Enter para manter o atual): ") or None
                description = input("Digite a nova descrição do produto (ou pressione Enter para manter a atual): ") or None
                price = input("Digite o novo preço do produto (ou pressione Enter para manter o atual): ")
                price = float(price) if price else None
                stock = input("Digite o novo estoque do produto (ou pressione Enter para manter o atual): ")
                stock = int(stock) if stock else None
                update_product(product_id, name, description, price, stock)
            case "5":
                product_id = input("Digite o ID do produto: ")
                delete_product(product_id)
            case "0":
                print("Saindo...")
                break
            case _:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
