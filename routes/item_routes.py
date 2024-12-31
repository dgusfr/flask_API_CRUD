from flask import Blueprint
from controllers.item_controller import get_items, create_item, update_item, delete_item

item_routes = Blueprint('item_routes', __name__)

item_routes.route('/items', methods=['GET'])(get_items)
item_routes.route('/items', methods=['POST'])(create_item)
item_routes.route('/items/<int:item_id>', methods=['PUT'])(update_item)
item_routes.route('/items/<int:item_id>', methods=['DELETE'])(delete_item)
