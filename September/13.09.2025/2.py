import requests # библиотека для заппросв в интернет
from bs4 import BeautifulSoup # библиотека для парсинга

data = []

url = "https://quotes.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")
quotes = soup.find_all("div", class_="quote") # find_all - Отображает все цитаты
# print(len(quotes))

# Делаем цикл для каждой цитаты в цитатах
for quote in quotes:
    quote_text = quote.find("span", class_= "text").get_text(strip=True)# Теперь в этой переменной показывается только текст нашей цитаты
    quote_author = quote.find("small", class_= "author").get_text(strip=True)

    # print(quote_author.ljust(20, " "), quote_text) # 20 Количество символов в строке, " остальное заполняется пробелами"

    d = {"author": quote_author, "quote": quote_text}
    data.append(d) # Добавили дату


for elem in data: # разделили каждую цитату и автора по словарям с ключом и значением
    print(elem)
