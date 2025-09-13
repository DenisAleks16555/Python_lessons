import requests # библиотека для заппросв в интернет
from bs4 import BeautifulSoup # библиотека для парсинга

url = "https://quotes.toscrape.com/"
response = requests.get(url)

# print(response.status_code)
# print(response.txt) # Можем получить всю страницу сайта

soup = BeautifulSoup(response.text, "lxml")
# print(soup.text) # Забирает весь текст из html файла
# print(soup.prettify()) # преобразовывает нашу html стрваницу в красивый вид


quote = soup.find("div", class_="quote")
# print(quote.text)
# print(quote.prettify())

quote_text = quote.find("span", class_= "text").get_text(strip=True)# Теперь в этой переменной показывается только текст нашей цитаты
quote_author = quote.find("small", class_= "author").get_text(strip=True)
print(quote_text) 
print(quote_author) 