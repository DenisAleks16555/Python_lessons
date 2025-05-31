# Задачка
worker = {
    "name": "Иван",
    "fname": "Иванов",
    "age": 25,
    "profession": "Баскетболист",
    "salary": 500_000

}

worker["star_date"] = "12.12.12"# Добавление в наш словарь ключа и значения

print(worker)

print(f"{worker['profession']}, по фамилии {worker['fname']}, получает зарплату  {worker['salary']} евро")