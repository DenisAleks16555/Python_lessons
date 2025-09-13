import json

# Читаем данные из файла
with open(r"C:\Users\0\OneDrive\Рабочий стол\MyPythonProjects\Python_lessons\12.08.2025\project_3\people.json", 'r', encoding='utf-8') as file:
    people = json.load(file)

# Инициализируем первого человека как самого старшего
oldest_person = people[0]

# Проходим по всем людям
for person in people:
    # Если текущий человек старше, обновляем oldest_person
    if person['age'] > oldest_person['age']:
        oldest_person = person

# Выводим результат
print(f"Самый старший человек: {oldest_person['name']}, возраст: {oldest_person['age']} лет")