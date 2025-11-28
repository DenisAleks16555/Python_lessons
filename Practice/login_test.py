from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Путь к драйверу: файл в той же папке
driver_path = 'msedgedriver.exe'

# Создаём сервис для драйвера
service = Service(executable_path=driver_path)

# Опции для Edge
options = Options()

try:
    # Запускаем браузер
    driver = webdriver.Edge(service=service, options=options)
    print("Браузер Edge запущен успешно!")

    # Переходим на сайт
    driver.get("https://practicetestautomation.com/practice-test-login/")
    print("Сайт открыт!")

    # Скриншот после открытия сайта
    driver.save_screenshot('after_open.png')
    print("Скриншот сохранён: after_open.png")

    # Ждём загрузки страницы
    time.sleep(2)

    # Находим поля и заполняем правильными данными
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "submit")

    username_field.send_keys("student")  # Правильный username
    password_field.send_keys("Password123")  # Правильный password
    login_button.click()

    # Выводим URL после клика для отладки
    print("Текущий URL после клика:", driver.current_url)

    # Ждём изменения URL (до 10 секунд)
    try:
        WebDriverWait(driver, 10).until(EC.url_contains("logged-in-successfully"))
        print("URL изменился — логин удался!")

        # Скриншот после успешного логина
        driver.save_screenshot('after_login.png')
        print("Скриншот сохранён: after_login.png")

        # Теперь ищем элемент post-title
        success_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "post-title"))
        )
        success_message = success_element.text
        print(f"Сообщение после входа: {success_message}")

    except:
        # Если URL не изменился, проверяем ошибку на странице входа
        print("URL не изменился — логин не удался.")
        try:
            error_element = driver.find_element(By.ID, "error")
            error_message = error_element.text
            print(f"Ошибка на странице: {error_message}")
        except:
            print("Сообщение об ошибке не найдено. Проверьте страницу вручную.")

    # Закрываем браузер
    driver.quit()
    print("Тест завершён!")

except Exception as e:
    print(f"Ошибка: {e}")
    if 'driver' in locals():
        driver.quit()

input("Нажмите Enter, чтобы закрыть...")  # Чтобы консоль не закрывалась сразу










# from selenium import webdriver
# from selenium.webdriver.edge.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.edge.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# # Путь к драйверу: файл в той же папке
# driver_path = 'msedgedriver.exe'

# # Создаём сервис для драйвера
# service = Service(executable_path=driver_path)

# # Опции для Edge
# options = Options()

# try:
#     # Запускаем браузер
#     driver = webdriver.Edge(service=service, options=options)
#     print("Браузер Edge запущен успешно!")

#     # Переходим на сайт
#     driver.get("https://practicetestautomation.com/practice-test-login/")
#     print("Сайт открыт!")

#     # Ждём загрузки страницы
#     time.sleep(2)

#     # Находим поля и заполняем правильными данными
#     username_field = driver.find_element(By.ID, "username")
#     password_field = driver.find_element(By.ID, "password")
#     login_button = driver.find_element(By.ID, "submit")

#     username_field.send_keys("student")  # Правильный username
#     password_field.send_keys("Password123")  # Правильный password
#     login_button.click()

#     # Выводим URL после клика для отладки
#     print("Текущий URL после клика:", driver.current_url)

#     # Ждём изменения URL (до 10 секунд)
#     try:
#         WebDriverWait(driver, 10).until(EC.url_contains("logged-in-successfully"))
#         print("URL изменился — логин удался!")

#         # Теперь ищем элемент post-title
#         success_element = WebDriverWait(driver, 5).until(
#             EC.presence_of_element_located((By.CLASS_NAME, "post-title"))
#         )
#         success_message = success_element.text
#         print(f"Сообщение после входа: {success_message}")

#     except:
#         # Если URL не изменился, проверяем ошибку на странице входа
#         print("URL не изменился — логин не удался.")
#         try:
#             error_element = driver.find_element(By.ID, "error")
#             error_message = error_element.text
#             print(f"Ошибка на странице: {error_message}")
#         except:
#             print("Сообщение об ошибке не найдено. Проверьте страницу вручную.")

#     # Закрываем браузер
#     driver.quit()
#     print("Тест завершён!")

# except Exception as e:
#     print(f"Ошибка: {e}")
#     if 'driver' in locals():
#         driver.quit()

# input("Нажмите Enter, чтобы закрыть...")  # Чтобы консоль не закрывалась сразу















# from selenium import webdriver  # Это библиотека для управления браузером
# from selenium.webdriver.edge.service import Service  # Для работы с Edge
# from selenium.webdriver.common.by import By  # Для поиска элементов на странице
# from selenium.webdriver.support.ui import WebDriverWait  # Для ожидания загрузки
# from selenium.webdriver.support import expected_conditions as EC  # Для условий ожидания

# # Шаг 1: Укажите путь к драйверу Edge (msedgedriver.exe)
# # Замените 'path/to/msedgedriver.exe' на реальный путь к файлу, который вы скачали.
# # Например: 'C:\\Users\\ВашеИмя\\Desktop\\msedgedriver.exe'
# driver_path = 'C:/Users/0/OneDrive/Рабочий стол/MyPythonProjects/Python_lessons/Practice'#'path/to/msedgedriver.exe'  # Вставьте сюда свой путь!

# # Шаг 2: Запустите браузер Edge
# service = Service(driver_path)
# driver = webdriver.Edge(service=service)

# # Шаг 3: Откройте страницу логина
# driver.get('https://practicetestautomation.com/practice-test-login/')

# # Шаг 4: Найдите поле для логина и введите текст
# # Мы ищем поле по его имени (name="username")
# username_field = driver.find_element(By.NAME, 'username')
# username_field.send_keys('student')  # Введите логин

# # Шаг 5: Найдите поле для пароля и введите текст
# # Мы ищем поле по его имени (name="password")
# password_field = driver.find_element(By.NAME, 'password')
# password_field.send_keys('Password123')  # Введите пароль

# # Шаг 6: Найдите кнопку "Submit" и нажмите её
# # Мы ищем кнопку по её ID (id="submit")
# submit_button = driver.find_element(By.ID, 'submit')
# submit_button.click()

# # Шаг 7: Подождите, пока страница загрузится после входа
# # Мы ждём, пока появится элемент с текстом "Logged In Successfully" (или похожий)
# wait = WebDriverWait(driver, 10)  # Ждём до 10 секунд
# success_message = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'post-title')))  # Ищем заголовок после входа

# # Шаг 8: Возьмите информацию со страницы (например, заголовок)
# page_title = driver.find_element(By.CLASS_NAME, 'post-title').text  # Текст заголовка
# print("Информация после входа:", page_title)  # Выведем в консоль

# # Шаг 9: Закройте браузер
# driver.quit()
