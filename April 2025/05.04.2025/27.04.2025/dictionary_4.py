# Метод update
worker = {
    "name": "Иван",
    "age": 25
}

worker1 = {
    "name": "Антон",
    "fname": "Иванов"
}

#worker.update(worker1) # Перезаписываем если одинаковые ключи
worker |= worker1 # То же самое метод update
print(worker)