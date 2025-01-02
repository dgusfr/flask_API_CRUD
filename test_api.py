import requests

URL = "http://127.0.0.1:5000/products"

def list_products():
  response = requests.get(URL)
  if response.status == 200:
    print("Produtos disponiveis")
    for product in  response.json():
      print(f"- ID: {product['id']}, Nome: {product['name']}, Estoque: {product['stock']}")
    else:
      print("Erro ao listar produtos:", response.status_code, response.text)