from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import json

# Настройки браузера (убрал --headless для отладки — верни, если работает)
options = webdriver.EdgeOptions()
# options.add_argument("--headless")  # Временно убрал для проверки
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

# Инициализация драйвера
driver = webdriver.Edge(options=options)

# Открываем сайт
driver.get("http://quotes.toscrape.com/")

# Список для результатов
results = []

# Инициализация счётчика страниц
page_count = 1

while True:
    # Печатаем текущую страницу
    print(f"Парсим страницу {page_count}")
    
    # Парсим цитаты на текущей странице
    quotes = driver.find_elements(By.CLASS_NAME, "quote")
    print(f"Найдено цитат на странице: {len(quotes)}")
    
    for quote in quotes:
        text = quote.find_element(By.CLASS_NAME, "text").text
        author = quote.find_element(By.CLASS_NAME, "author").text
        tags = [tag.text for tag in quote.find_elements(By.CLASS_NAME, "tag")]
        
        results.append({
            "text": text,
            "author": author,
            "tags": tags
        })
    
    # Ищем кнопку "Next" (исправил селектор: PARTIAL_LINK_TEXT, "Next")
    try:
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Next"))
        )
        print("Кнопка Next найдена, кликаем...")
        next_button.click()
        
        # Увеличиваем счётчик после клика
        page_count += 1
        
        # Ожидание загрузки новой страницы (теперь ждём изменения URL)
        WebDriverWait(driver, 10).until(
            lambda d: "/page/" in d.current_url  # Ждём, пока URL изменится на /page/X/
        )
        print(f"Перешли на страницу {page_count}")
        
    except TimeoutException:
        print("Больше страниц нет — парсинг закончен.")
        break

# Сохраняем результаты в JSON
with open("quotes.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=4)

print(f"Парсинг завершён. Всего цитат: {len(results)}")

# Закрываем браузер
driver.quit()




# import json
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.edge.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# # Настраиваем опции для браузера Edge (чтобы работал без графического интерфейса)
# options = Options()
# options.add_argument("--headless")  # Запуск без окна браузера
# options.add_argument("--disable-gpu")  # Для стабильности
# options.add_argument("--no-sandbox")

# # Создаём драйвер для Edge (убедись, что msedgedriver.exe в той же папке или в PATH)
# driver = webdriver.Edge(options=options)

# # Открываем сайт
# driver.get("http://quotes.toscrape.com/")
# print("Страница загружена!")

# # Ждём и находим все цитаты на первой странице
# quotes_elements = WebDriverWait(driver, 10).until(
#     EC.presence_of_all_elements_located((By.CLASS_NAME, "quote"))
# )
# print(f"Найдено цитат на первой странице: {len(quotes_elements)}")

# # Создаём список для результатов (здесь будут все цитаты со всех страниц)
# results = []

# # Проходим по каждой цитате на первой странице и собираем данные
# for quote in quotes_elements:
#     # Находим автора
#     author_element = quote.find_element(By.CLASS_NAME, "author")
#     author = author_element.text
    
#     # Находим текст цитаты
#     quote_text = quote.find_element(By.CLASS_NAME, "text").text
    
#     # Находим теги
#     tags_elements = quote.find_elements(By.CLASS_NAME, "tag")
#     tags = [tag.text for tag in tags_elements]
    
#     # Находим ссылку на автора
#     author_link = quote.find_element(By.CSS_SELECTOR, "a[href*='/author/']").get_attribute("href")
    
#     # Добавляем в список результатов
#     results.append({
#         "author": author,
#         "quote": quote_text,
#         "tags": tags,
#         "author_link": author_link
#     })

# # НОВЫЙ КОД: Теперь начинаем "листать" следующие страницы (после парсинга первой)
# while True:  # Это петля: повторяем, пока есть кнопка "Next"
#     try:
#         # Ищем кнопку "Next" на текущей странице
#         next_button = WebDriverWait(driver, 5).until(
#             EC.element_to_be_clickable((By.CSS_SELECTOR, "li.next a"))  # Селектор для кнопки "Next"
#         )
        
#         # Если кнопка найдена, кликаем на неё
#         next_button.click()
#         print("Кликнули 'Next', загружаем следующую страницу...")
        
#         # Ждём, пока новая страница загрузится (ждём новые цитаты)
#         WebDriverWait(driver, 10).until(
#             EC.presence_of_all_elements_located((By.CLASS_NAME, "quote"))
#         )
        
#         # Теперь парсим цитаты с новой страницы (то же самое, что и для первой)
#         quotes_elements = driver.find_elements(By.CLASS_NAME, "quote")
#         print(f"Найдено цитат на новой странице: {len(quotes_elements)}")
        
#         # Проходим по каждой новой цитате и добавляем в results
#         for quote in quotes_elements:
#             # Находим автора
#             author_element = quote.find_element(By.CLASS_NAME, "author")
#             author = author_element.text
            
#             # Находим текст цитаты
#             quote_text = quote.find_element(By.CLASS_NAME, "text").text
            
#             # Находим теги
#             tags_elements = quote.find_elements(By.CLASS_NAME, "tag")
#             tags = [tag.text for tag in tags_elements]
            
#             # Находим ссылку на автора
#             author_link = quote.find_element(By.CSS_SELECTOR, "a[href*='/author/']").get_attribute("href")
            
#             # Добавляем в список результатов
#             results.append({
#                 "author": author,
#                 "quote": quote_text,
#                 "tags": tags,
#                 "author_link": author_link
#             })
        
#     except:  # Если кнопки "Next" нет (или ошибка), выходим из петли
#         print("Больше страниц нет — парсинг закончен.")
#         break  # Это значит "стоп, выходи из петли"

# # После сбора всех цитат со всех страниц, сохраняем в JSON
# with open("quotes.json", "w", encoding="utf-8") as f:
#     json.dump(results, f, ensure_ascii=False, indent=4)

# print("Готово! Данные сохранены в quotes.json")

# # Закрываем браузер
# driver.quit()
