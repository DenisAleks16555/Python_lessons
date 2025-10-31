from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import time

def task1():
    print(f"[{datetime.now()}] Задача 1 выполняется!")

def task2():
    print(f"[{datetime.now()}] Задача 2 выполняется!")

scheduler = BackgroundScheduler()

# Добавляем задачи с id для управления
scheduler.add_job(task1, 'interval', seconds=5, id='job1')
scheduler.add_job(task2, 'interval', seconds=8, id='job2')

scheduler.start()

# Ждём 15 секунд, потом ставим первую задачу на паузу
time.sleep(15)
print(f"[{datetime.now()}] Ставим Задачу 1 на паузу")
scheduler.pause_job('job1')

# Ждём ещё 15 секунд (всего 30), потом удаляем обе задачи
time.sleep(15)
print(f"[{datetime.now()}] Удаляем обе задачи")
scheduler.remove_job('job1')
scheduler.remove_job('job2')

# Ждём ещё 10 секунд, чтобы увидеть, что задачи не выполняются
time.sleep(10)

scheduler.shutdown()

