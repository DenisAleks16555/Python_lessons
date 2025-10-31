from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import time

def hello(Den):
     # Печатаем V-знак как эмодзи ✌️
    print("✌️")
    print(f"[{datetime.now()}] Привет, {Den}!")

scheduler = BackgroundScheduler()
# Запускаем функцию hello каждые 7 секунд с параметром 'Аня' (замени на своё имя)
scheduler.add_job(hello, 'interval', seconds=7, args=['Den'])

scheduler.start()

time.sleep(22)  # Ждём 22 секунды, чтобы увидеть 3 запуска

scheduler.shutdown()
