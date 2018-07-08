import json

with open('config.json', 'r') as f:
    json_dict = json.load(f)
    print(json_dict)
    print(type(json_dict))