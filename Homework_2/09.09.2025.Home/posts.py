import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts?userId=1")
posts = response.json()

print("Post titles by user 1:")
for post in posts:
    print(post['title'])