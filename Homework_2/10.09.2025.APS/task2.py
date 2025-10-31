from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import time

def print_time():
    print(f"[{datetime.now()}] Сейчас время: {datetime.now().strftime('%H:%M:%S')}")

scheduler = BackgroundScheduler()
# Добавляем задачу с интервалом 5 секунд
scheduler.add_job(print_time, 'interval', seconds=5)

scheduler.start()

# Ждём 20 секунд, чтобы увидеть несколько запусков
time.sleep(20)

scheduler.shutdown()