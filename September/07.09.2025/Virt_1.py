from dotenv import load_dotenv
import os 

load_dotenv()

api_key = os.getenv("API_KEY")
login = os.getenv("LOGIN", "username")
password = os.getenv("PASSWORD", "password") # Первое ссылка на переменную, а второе, если переменная не найдена подставится значение по умолчанию


print(api_key)
print(login)
print(password)