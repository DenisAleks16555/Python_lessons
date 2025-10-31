from apscheduler.schedulers.background import BackgroundScheduler  # Импорт планировщика (как будильник)
from datetime import datetime, timedelta  # Импорт для работы со временем
import time  # Импорт для паузы (чтобы программа не закрылась сразу)

# Это функция, которую мы запустим через 10 секунд
def my_job():
    # Печатаем сообщение с текущим временем
    print(f"[{datetime.now()}] Время вышло!")

# Создаём планировщик (он работает в фоне, не мешает другим частям программы)
scheduler = BackgroundScheduler()

# Вычисляем время через 10 секунд: текущее время + 10 секунд
run_time = datetime.now() + timedelta(seconds=10)

# Добавляем задачу: запустить функцию my_job один раз в время run_time
scheduler.add_job(my_job, 'date', run_date=run_time)

# Запускаем планировщик
scheduler.start()

# Ждём 15 секунд (чтобы задача успела выполниться, и программа не закрылась)
time.sleep(15)

# Останавливаем планировщик (по желанию, но для чистоты)
scheduler.shutdown()
