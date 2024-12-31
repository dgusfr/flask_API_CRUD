import json

def read_json():
    with open('database.json', 'r') as file:
        return json.load(file)
