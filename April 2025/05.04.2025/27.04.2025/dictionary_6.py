# Метод setdefault
worker = {
    "name": "Иван",
    "fname": "Иванов",
    "profession": "Баскетболист",
    "salary": 500_000

}

worker.setdefault("age", 0) # установить по умолчанию
worker.setdefault("age", 30) 

print(worker)

# Метод pop удаляет что-то
name = worker.pop("name")
print(f"Удалили из словаря {name}")
print(worker)

# Метод popitem удаляет из словаря последний добавленный ключ
name = worker.popitem()
print(f"Удалили из словаря {name}")
print(worker)

# # Метод clear очищает полностью словарь - делает словарь пустым
# worker.clear()
# print(worker)

# Метод copy
# worker1 = worker

# worker1.clear()
# print(worker)
# print(worker1) так работать не будет

worker1 = worker.copy()
worker1["age"] = 100
print(worker)
print(worker1)
