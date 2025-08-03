import json

data = {
    "name": "Sharik",
    "age": 3,
    "color": "green"
}

json_data = json.dumps(data) # преобразование нашего файла в формат json
print(json_data)