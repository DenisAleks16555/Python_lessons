# Методы словарей:
worker = {
    "name": "Иван",
    "fname": "Иванов",
    "profession": "Баскетболист",
    "salary": 500_000

}
# if "age" in worker:
#     print(worker["age"])
# else:
#     print("not found")

print(worker.get("age")) # Этим методом мы заменяем верхний метод
print(worker.get("age", "not found"))


