from flask import Blueprint, request
from controllers.product_controller import ProductController

product_routes = Blueprint('product_routes', __name__)

# Rotas corrigidas para passar dados corretamente
@product_routes.route('/products', methods=['GET'])
def get_products():
    return ProductController.get_products()

@product_routes.route('/products/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    return ProductController.get_product_by_id(product_id)

@product_routes.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    return ProductController.create_product(data)

@product_routes.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    return ProductController.update_product(product_id, data)

@product_routes.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    return ProductController.delete_product(product_id)
