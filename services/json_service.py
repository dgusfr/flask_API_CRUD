import json

def read_json():
    with open('database.json', 'r') as file:
        return json.load(file)

def write_json(data):
    with open('database.json', 'w') as file:
        json.dump(data, file, indent=4)
