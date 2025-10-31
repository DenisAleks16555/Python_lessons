# Это начало: мы говорим Python, что нам нужны инструменты
from selenium import webdriver  # Selenium помогает открывать браузер и "читать" сайт
from selenium.webdriver.edge.options import Options  # Настройки для браузера Edge
from selenium.webdriver.common.by import By  # Помогает искать части сайта (как кнопки или текст)
from selenium.webdriver.support.ui import WebDriverWait  # Для ожидания загрузки страницы
from selenium.webdriver.support import expected_conditions as EC  # Условия ожидания
import json  # Это для сохранения данных в файл JSON (как сохранить список покупок в текстовый файл)
import time  # Для паузы (чтобы сайт успел загрузиться)

print("Инициализация настроек браузера...")  # Отладка: начало

# Настройки для браузера Edge (чтобы он открывался без лишних окон и работал стабильнее)
options = Options()  # Создаём "настройки" для браузера
options.add_argument("--disable-web-security")  # Отключаем некоторые проверки безопасности
options.add_argument("--disable-features=VizDisplayCompositor")  # Для стабильности
# options.add_argument("--headless")  # Пока убрал, чтобы ты видел браузер. Верни, если не нужно окно

print("Открываем браузер...")  # Отладка: перед запуском
# Шаг 1: Открываем браузер (Edge)
driver = webdriver.Edge(options=options)  # С опциями для стабильности
print("Браузер открыт.")  # Отладка: браузер запустился

# Шаг 2: Заходим на сайт с цитатами
print("Загружаем страницу...")  # Отладка: перед get
driver.get("https://quotes.toscrape.com/")  # Это как ввести адрес в браузере и нажать Enter — открываем сайт
print("Страница загружена, ждём элементы...")  # Отладка: страница открыта

# Ждём, пока хотя бы один элемент "quote" загрузится (до 10 секунд)
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "quote")))
    print("Элементы найдены, продолжаем...")  # Отладка: ожидание прошло
except Exception as e:
    print(f"Ошибка ожидания элементов: {e}")  # Если не загрузилось за 10 сек — ошибка
    driver.quit()  # Закрываем браузер
    exit()  # Выходим из программы

# Шаг 3: Ищем все цитаты на странице
quotes_elements = driver.find_elements(By.CLASS_NAME, "quote")  # quotes_elements — список всех цитат
print(f"Найдено цитат: {len(quotes_elements)}")  # Отладка: сколько нашли

# Шаг 4: Для каждой цитаты берём нужные данные и складываем в список
results = []  # Пустой список, куда будем класть данные о цитатах
for quote_element in quotes_elements:  # Проходим по каждой цитате
    try:
        # Берём текст цитаты: ищем внутри блока элемент с классом "text" и берём его текст
        quote_text = quote_element.find_element(By.CLASS_NAME, "text").text
        
        # Берём автора: ищем элемент с классом "author" и берём его текст
        author = quote_element.find_element(By.CLASS_NAME, "author").text
        
        # Берём ссылку на страницу автора: ищем ссылку с "/author/" в href (исправленный селектор)
        author_url = quote_element.find_element(By.CSS_SELECTOR, "a[href*='/author/']").get_attribute("href")
        
        # Берём все теги: ищем блок с тегами (класс "tags"), внутри него все элементы с классом "tag"
        tags_elements = quote_element.find_element(By.CLASS_NAME, "tags").find_elements(By.CLASS_NAME, "tag")
        tags = [tag.text for tag in tags_elements]
        
        # Складываем всё в "коробку" (словарь)
        quote_data = {
            "author": author,
            "quote": quote_text,
            "tags": tags,
            "author_url": author_url
        }
        results.append(quote_data)
        print(f"Обработана цитата: {author} - {quote_text[:30]}...")  # Отладка: что обработали
    except Exception as e:
        print(f"Ошибка при обработке цитаты: {e}")  # Печатаем ошибку

# Шаг 5: Красиво выводим данные в консоль
print("Список цитат:")  # Заголовок
print("-" * 100)  # Линия
for result in results:
    author_str = result["author"].ljust(20)
    quote_str = (result["quote"][:50] + "..." if len(result["quote"]) > 50 else result["quote"]).ljust(55)
    tags_str = ", ".join(result["tags"]).ljust(30)
    url_str = result["author_url"]
    print(f"{author_str} | {quote_str} | {tags_str} | {url_str}")

# Шаг 6: Сохраняем данные в файл quotes.json
with open("quotes.json", "w", encoding="utf-8") as file:
    json.dump(results, file, indent=4, ensure_ascii=False)

# Шаг 7: Закрываем браузер
driver.quit()

print("\nГотово! Данные сохранены в quotes.json")  # Финальное сообщение
