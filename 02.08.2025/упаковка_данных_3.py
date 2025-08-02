import json


json_data = '{"name": "Sharik", "age": 3, "color": "green"}'

# Конвертируем эту строку в объект
data = json.loads(json_data) # .loads - загружает json объект из строки и конвертирует её в объекты языка Python 

print(data["name"])
print(type(data))