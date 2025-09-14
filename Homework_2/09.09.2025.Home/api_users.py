import requests  # Импортируем библиотеку для работы с интернет-запросами

# URL сайта, к которому мы обращаемся (ресурс /users для списка пользователей)
url = "https://jsonplaceholder.typicode.com/users"

# Отправляем GET-запрос (получаем данные)
response = requests.get(url)

# Проверяем, успешен ли запрос (код 200 значит "всё OK")
if response.status_code == 200:
    # Преобразуем ответ в JSON (из текста в удобный формат Python)
    users = response.json()
    
    # Красиво выводим JSON (с отступами для читаемости)
    import json  # Импортируем для красивого вывода
    print(json.dumps(users, indent=4))  # indent=4 добавляет отступы
else:
    # Если ошибка, выводим код ошибки
    print(f"Ошибка: {response.status_code}")