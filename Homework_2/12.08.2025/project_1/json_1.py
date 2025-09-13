import json

# Создаем словарь
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Открываем файл для записи и сохраняем словарь в формате JSON
with open('person.json', 'w', encoding='utf-8') as file:
    json.dump(person, file)