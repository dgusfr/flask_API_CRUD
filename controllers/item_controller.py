from flask import jsonify
from services.json_service import read_json

def get_items():
    data = read_json()
    return jsonify(data['items'])
