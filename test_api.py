import requests

BASE_URL = "http://127.0.0.1:5000/products"

def create_product(name, description, price, stock):
    data = {"name": name, "description": description, "price": price, "stock": stock}
    response = requests.post(BASE_URL, json=data)
    try:
        print(f"Create Product Response: {response.status_code}, {response.json()}")
    except requests.exceptions.JSONDecodeError:
        print(f"Create Product Response: {response.status_code}, {response.text}")

def list_products():
    response = requests.get(BASE_URL)
    try:
        print(f"List Products Response: {response.status_code}, {response.json()}")
    except requests.exceptions.JSONDecodeError:
        print(f"List Products Response: {response.status_code}, {response.text}")

def update_product(product_id, name=None, description=None, price=None, stock=None):
    data = {key: value for key, value in locals().items() if value is not None and key != "product_id"}
    response = requests.put(f"{BASE_URL}/{product_id}", json=data)
    try:
        print(f"Update Product Response: {response.status_code}, {response.json()}")
    except requests.exceptions.JSONDecodeError:
        print(f"Update Product Response: {response.status_code}, {response.text}")

def delete_product(product_id):
    response = requests.delete(f"{BASE_URL}/{product_id}")
    try:
        print(f"Delete Product Response: {response.status_code}, {response.json()}")
    except requests.exceptions.JSONDecodeError:
        print(f"Delete Product Response: {response.status_code}, {response.text}")

if __name__ == "__main__":
    print("Creating a new product...")
    create_product("Notebook", "High-performance laptop", 1999.99, 10)

    print("\nListing all products...")
    list_products()

    print("\nUpdating a product...")
    update_product(1, price=1799.99, stock=15)

    print("\nListing all products after update...")
    list_products()

    print("\nDeleting a product...")
    delete_product(1)

    print("\nListing all products after deletion...")
    list_products()
