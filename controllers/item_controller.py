from flask import request, jsonify
from services.json_service import read_json, write_json

def create_item():
    data = read_json()
    new_item = request.json
    new_item['id'] = len(data['items']) + 1
    data['items'].append(new_item)
    write_json(data)
    return jsonify(new_item), 201
