import os
print(os.getcwd())


import json

# Шаг 1. Открываем файл и читаем список пользователей
with open(r"C:\Users\0\OneDrive\Рабочий стол\MyPythonProjects\Python_lessons\12.08.2025\project_4\users.json", 'r', encoding='utf-8') as file:
    users = json.load(file)
# with open('users.json', 'r', encoding='utf-8') as file:
#     users = json.load(file)  # читаем содержимое файла и превращаем его в список Python

# Шаг 2. Запрашиваем у пользователя имя и email нового пользователя
new_username = input("Введите имя нового пользователя: ")
new_email = input("Введите email нового пользователя: ")

# Создаем словарь с данными нового пользователя
new_user = {
    "username": new_username,
    "email": new_email
}

# Шаг 3. Добавляем нового пользователя в список
users.append(new_user)

# Шаг 4. Записываем обновленный список обратно в файл
with open('users.json', 'w', encoding='utf-8') as file:
    json.dump(users, file, ensure_ascii=False, indent=4)

print("Пользователь успешно добавлен!")