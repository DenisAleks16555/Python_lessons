import json  # Модуль для работы с JSON
import os    # Модуль для работы с путями к файлам

# Шаг 1: Получаем путь к папке, где лежит этот скрипт
script_dir = os.path.dirname(os.path.abspath(__file__))

# Шаг 2: Формируем полный путь к файлу config.json в той же папке
json_path = os.path.join(script_dir, 'config.json')

# Шаг 3: Открываем и читаем JSON-файл
with open(json_path, 'r', encoding='utf-8') as file:
    config = json.load(file)  # Загружаем данные в словарь config

# Шаг 4: Проверяем, есть ли ключ "debug" в словаре
if "debug" in config:
    print("Ключ 'debug' уже есть в файле!")  # Если есть, просто сообщаем
else:
    config["debug"] = False  # Если нет, добавляем ключ со значением False
    print("Ключ 'debug' добавлен со значением False.")

# Шаг 5: Сохраняем обновлённый словарь обратно в файл
with open(json_path, 'w', encoding='utf-8') as file:
    json.dump(config, file, indent=4)  # indent=4 делает файл красивым (с отступами)

print("Файл обновлён!")  # Сообщение о завершении