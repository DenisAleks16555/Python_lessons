import requests
import json

# Адрес сайта
url = 'https://jsonplaceholder.typicode.com/posts/1'

# Данные для обновления
data = {
    "title": "foo"
}

# Отправляем PATCH-запрос
response = requests.patch(url, json=data)

# Получаем обновлённый пост
updated_post = response.json()

# Выводим обновлённый заголовок красиво
print("Updated title:", json.dumps(updated_post['title'], indent=4, ensure_ascii=False))