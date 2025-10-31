from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import time

def reminder():
    print(f"[{datetime.now()}] Напоминание!")

scheduler = BackgroundScheduler()
# Запускаем задачу каждую минуту
scheduler.add_job(reminder, 'cron', minute='*/1')

scheduler.start()

# Ждём 3 минуты (180 секунд)
time.sleep(180)

scheduler.shutdown()