import requests # библиотека для заппросв в интернет
from bs4 import BeautifulSoup # библиотека для парсинга

# Здесь парсим одну страницу
base_url = "https://quotes.toscrape.com" # учебный сайт

response = requests.get(base_url)

soup = BeautifulSoup(response.text, "lxml")
quotes = soup.find_all("div", class_ = "quote") # find_all - Отображает все цитаты 

data = []

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
    print(url)
# print(next_btn.prettify())

