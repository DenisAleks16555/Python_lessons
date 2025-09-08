from apscheduler.schedulers.background import BackgroundScheduler # фоновый планировщик
import time
from datetime import datetime, timedelta

def say():
    print("Ежедневная задача")

scheduler = BackgroundScheduler()
scheduler.add_job(say, 'cron', hour=19, minute=4) # тригер "cron" -  запуск будет выполняться каждый день в 19 часов 04 минуты
scheduler.start()

while True: # функция бесконечности
    pass

