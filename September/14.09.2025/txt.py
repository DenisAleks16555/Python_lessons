import requests # библиотека для заппросв в интернет
from bs4 import BeautifulSoup # библиотека для парсинга
import time
data = []

base_url = "https://quotes.toscrape.com" # учебный сайт
url = base_url

while url:
    time.sleep(2)# Задержка парсинга(лучше ставить 5 секунд)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    quotes = soup.find_all("div", class_ = "quote") # find_all - Отображает все цитаты 


    # Делаем цикл для каждой цитаты в цитатах
    for quote in quotes:
        quote_text = quote.find("span", class_= "text").get_text(strip=True)# Теперь в этой переменной показывается только текст нашей цитаты
        quote_author = quote.find("small", class_= "author").get_text(strip=True)

        # print(quote_author.ljust(20, " "), quote_text) # 20 Количество символов в строке, " остальное заполняется пробелами"

        d = {"author": quote_author, "quote": quote_text}
        data.append(d) # Добавили дату

    next_btn = soup.find("li", class_= "next") # ищем кнопку переключения страницы и саму страницу
    if next_btn: 
        url = base_url + next_btn.a["href"] # Обращаемся к тегу а и берем параметр href(ключ), а зна
        # print(url)
    else: # Если не нашли кнопку Next, то завершаем цикл
        url = None

with open("quotes.txt", "w", encoding="utf-8") as fl:
    for elem in data:
        fl.write(
            f"{elem['author'].ljust(20, ' ')}{elem['quote']}\n"
                 )

print("--------------------------------------------")
print(f"Парсинг завершён, найдено {len(data)} цитат")