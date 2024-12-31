from flask import request, jsonify
from services.json_service import read_json, write_json

def get_items():
    data = read_json()
    return jsonify(data['items'])

def create_item():
    data = read_json()
    new_item = request.json
    new_item['id'] = len(data['items']) + 1
    data['items'].append(new_item)
    write_json(data)
    return jsonify(new_item), 201

def update_item(item_id):
    data = read_json()
    updated_item = request.json
    for item in data['items']:
        if item['id'] == item_id:
            item.update(updated_item)
            write_json(data)
            return jsonify(item)
    return jsonify({'error': 'Item not found'}), 404

def delete_item(item_id):
    data = read_json()
    data['items'] = [item for item in data['items'] if item['id'] != item_id]
    write_json(data)
    return jsonify({'message': 'Item deleted'}), 200
