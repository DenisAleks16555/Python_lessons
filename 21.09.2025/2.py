from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

driver = webdriver.Chrome()
driver.get("https://quotes.toscrape.com/scroll")

wait = WebDriverWait(driver, 10)

def count_quotes():
    return len(driver.find_elements(By.CSS_SELECTOR, ".qoute")) # Функция для просмотра прибавилось у нас элементов после прокрутки страницы вниз

prev_count = count_quotes()

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # Окно прокрутить  от 0 в самый низ страницы

    try:
        wait.until(lambda x: len(x.find_elements(By.CSS_SELECTOR, ".qoute") > prev_count)) # ждём пока количество страниц на странице будет больше до того как мы прокрутим страницу
        prev_count = count_quotes() # Считаем заново количество
        time.sleep(1)

    except Exception:
        break
data = []
for quote in driver.find_elements(By.CSS_SELECTOR, ".quote"):
    text = quote.find_element(By.CSS_SELECTOR, ".text").text # Извлекаем текст из этого всего
    author = quote.find_element(By.CSS_SELECTOR, ".author").text
    tags = ', '.join([t.text for t in quote.find_elements(By.CSS_SELECTOR, ".tag")]) # Ищем все теги и склеиваим их
    data.append((text, author, tags)) # Добавляем в конец списка этот кортеж



time.sleep(10)
driver.quit()

for elem in data:
    print(*elem, sep="\n")
    print()