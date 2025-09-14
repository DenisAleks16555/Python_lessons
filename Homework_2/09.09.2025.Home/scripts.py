import requests

# Отправляем запрос к сайту, чтобы получить комментарии
response = requests.get('https://jsonplaceholder.typicode.com/posts/1/comments')

if response.status_code == 200:
    comments = response.json()
    
    print("Comments for post 1:\n")
    for comment in comments:
        print(f"{comment['name']} — {comment['body']}")
else:
    print("Что-то пошло не так")