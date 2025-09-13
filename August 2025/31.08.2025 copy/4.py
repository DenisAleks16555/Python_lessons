from apscheduler.schedulers.background import BackgroundScheduler # фоновый планировщик
import time
from datetime import datetime, timedelta

def say():
    print("Работа в фоне")

scheduler = BackgroundScheduler()
scheduler.add_job(say, 'date', run_date = datetime.now() + timedelta(seconds=5)) # тригер "date" - единаразовый запуск через 5 секунд
scheduler.start()

while True: # функция бесконечности
    pass

