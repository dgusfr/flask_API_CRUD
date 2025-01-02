from flask import Blueprint
from controllers.product_controller import ProductController

product_routes = Blueprint('product_routes', __name__)

product_routes.route('/products', methods=['GET'])(ProductController.get_products)
product_routes.route('/products', methods=['POST'])(ProductController.create_product)
product_routes.route('/products/<int:product_id>', methods=['PUT'])(ProductController.update_product)
product_routes.route('/products/<int:product_id>', methods=['DELETE'])(ProductController.delete_product)
