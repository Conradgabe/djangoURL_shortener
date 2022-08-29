import uuid

def generate_uuid():
    url = str(uuid.uuid4())[:6]
    return url