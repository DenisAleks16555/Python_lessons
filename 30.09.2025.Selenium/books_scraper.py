# Это начало: мы говорим Python, что нам нужны инструменты
from selenium import webdriver  # Selenium помогает управлять браузером
from selenium.webdriver.edge.options import Options  # Импорт для настройки Edge
from selenium.webdriver.common.by import By  # Это для поиска элементов на странице (как кнопки или текст)

# Настройки для Edge
options = Options()


# Шаг 1: Открываем браузер (Edge вместо Chrome)
driver = webdriver.Edge(options=options)  # Запускаем Edge через наш код (убедись, что msedgedriver.exe в той же папке)

# Шаг 2: Заходим на сайт
driver.get("http://books.toscrape.com/")  # Это как ввести адрес в браузере и нажать Enter

# Шаг 3: Ищем все книги на странице
# Сайт показывает книги в контейнерах. Мы используем подсказку: find_elements(By.CLASS_NAME, "product_pod")
# Это значит: "Найди все элементы, у которых класс (вид) называется 'product_pod'"
books = driver.find_elements(By.CLASS_NAME, "product_pod")  # books — список всех книг (как коробки с книгами)

# Шаг 4: Для каждой книги берём название и цену
results = []  # Пустой список, куда будем складывать данные (как пустая корзина)
for book in books:  # Проходим по каждой книге (как открыть каждую коробку)
    # Название: используем подсказку element.find_element(By.CSS_SELECTOR, "h3 a")
    # Это: "Внутри книги найди элемент с тегом h3, а внутри него — ссылку a"
    title_element = book.find_element(By.CSS_SELECTOR, "h3 a")  # Нашли ссылку
    title = title_element.get_attribute("title")  # Берём текст из атрибута "title" (название книги)
    
    # Цена: используем подсказку element.find_element(By.CSS_SELECTOR, ".price_color")
    # Это: "Найди элемент с классом 'price_color' (там цена)"
    price_element = book.find_element(By.CSS_SELECTOR, ".price_color")  # Нашли цену
    price = price_element.text  # Берём текст (например, "£51.77")
    
    # Складываем в словарь (как карточку с данными)
    book_data = {"title": title, "price": price}  # Словарь: ключ "title" — название, "price" — цена
    results.append(book_data)  # Добавляем в список

# Шаг 5: Выводим результаты в консоль
print("Найденные книги:")  # Просто текст для начала
for result in results:  # Проходим по списку и печатаем каждую
    print(result)  # Покажет, например, {'title': 'A Light in the Attic', 'price': '£51.77'}

# Шаг 6: Закрываем браузер
driver.quit()  # Выходим из браузера, чтобы не висел


