from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("http://selenium.dev") # Отправляем запрос

time.sleep(30) # Задержка между следующей командой

driver.quit() # Закрыли браузер(Выход)