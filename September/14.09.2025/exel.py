import requests # библиотека для заппросв в интернет
from bs4 import BeautifulSoup # библиотека для парсинга
import time
import xlsxwriter

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
        print(url)
        # Парсим только одну страницу
        # url = None
    else: # Если не нашли кнопку Next, то завершаем цикл
        url = None

print("--------------------------------------------")
print(f"Парсинг завершён, найдено {len(data)} цитат")

workbook = xlsxwriter.Workbook("quotes.xlsx") # Пример  для записи в Exel Создали страницу
worksheet = workbook.add_worksheet("Quotes") # Создали вкладки в Exel

# Вариант номер один(простой)
# Создаём стиль форматирования
header_format = workbook.add_format(
    {
        "bold": True,
        "border": 1,
        "align": "center",
        "valign": "vcenter"
    })

text_format = workbook.add_format({
    "border": 1,
    "align": "left",
    "text_wrap": True # Отвечает за перенос строк
}
)


worksheet.set_column(0, 0, 25) # Установить размер(ширину) колонки с индексом 0 и 0
worksheet.set_column(1, 1, 300)
worksheet.set_row(0, 30) # Установить номер строки(0) высоту строк !!!


# Для записи информации в ячейки
worksheet.write(0, 0, "Author", header_format) # По индексу - 0 - номер строки 0 - номер колонки auothor верхний левый угол
worksheet.write(0, 1, "Quote", header_format) # По индексу - 0 - номер строки 0 - номер колонки

for row, elem in enumerate(data, start=1):  # функция перечисления
    worksheet.write(row, 0, elem["author"], text_format)
    worksheet.write(row, 1, elem["quote"], text_format)

workbook.close()

print("Файл Exel успешно создан")