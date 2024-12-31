def validate_item(data):
    if 'name' not in data or not isinstance(data['name'], str):
        return False, 'Invalid name'
    return True, None
