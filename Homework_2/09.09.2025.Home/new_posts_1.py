import requests

url = 'https://jsonplaceholder.typicode.com/posts'

post_data = {
    "title": "Мой заголовок",
    "body": "Текст",
    "userId": 5
}

response = requests.post(url, json=post_data)

# Выводим ответ, чтобы понять, что пришло
print(response.json())

# Получаем ID нового поста
new_post_id = response.json()['id']
print("Created post ID:", new_post_id)