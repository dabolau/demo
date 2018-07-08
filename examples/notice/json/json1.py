import json

json_dict = {
    'url': 'http://127.0.0.1:8000',
    'offset': '/ajax?name=实验室01',
    'mp3': 'jinggao.mp3',
    'location': '白居寺车场',
    'temperature': '30',
    'humidity': '80',
    'time': '5',
}

with open('config.json', 'w') as f:
    json.dump(json_dict, f)
    print('成功写入文件')