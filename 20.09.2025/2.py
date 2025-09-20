import requests
import time


base_url = "https://quotes.toscrape.com/api/quotes?page="

url = base_url + "1"

while url:
    time.sleep(2)
    response = requests.get(url) # Смотрим на сайте какой метод Get или Post

    if response.status_code != 200: # Смотрим на сайте какой код(200)
        print("Ошибка получения данных")
        break

    data = response.json() # Метод который преобразовывает json файл в словарь Python

    quotes = data["quotes"]

    for quote in quotes:
        print()
        print(quote.get("text", ""))
        print(quote['author']["name"])
        print(" - ".join(quote['tags'])) # Вернётся отдельной строкой
        print()



    next = data.get("has_next", False)
    next_page = data.get("page", False)

    if next and next_page: # Если у нас есть и тот ключ(next) и этот next_page
        url = base_url + str(next_page + 1) # Приведём к строке next_page
    else:
        url = None

    print(f"Переходим к странице №{next_page}...")



