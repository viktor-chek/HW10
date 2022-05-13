import json


def load_json(data):
    with open(data, encoding="utf-8") as f:
        data = json.load(f)
    return data
