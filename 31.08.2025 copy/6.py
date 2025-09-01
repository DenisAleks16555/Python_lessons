from apscheduler.schedulers.background import BackgroundScheduler # фоновый планировщик
import time
from datetime import datetime, timedelta 

def say():
    print("Ежедневная задача")

scheduler = BackgroundScheduler()
scheduler.add_job(
    say, 
    'cron', # Планировщик задач
    day_of_week='mon,wen', # будет выполняться каждый понедельник и среду
    months='1,2', # будет выполняться в январе и феврале
    hour='8-18/2', # с 8 до 18 часов /2 с переодичностью в два часа
    minute=0) # пример - с 8-00
scheduler.start()

while True: 
    pass

