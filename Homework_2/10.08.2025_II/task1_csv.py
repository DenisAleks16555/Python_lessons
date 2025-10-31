import csv  # Импортируем модуль для работы с CSV

# Список учеников
students = [
    {"name": "Alice", "age": 15, "grade": "A"},
    {"name": "Bob", "age": 14, "grade": "B"},
    {"name": "Charlie", "age": 15, "grade": "C"}
]

# Открываем файл для записи ('w' — write)
with open("students.csv", "w", newline="") as file:
    # Создаем объект для записи словарей в CSV
    writer = csv.DictWriter(file, fieldnames=["name", "age", "grade"])
    
    # Записываем заголовки (названия столбцов)
    writer.writeheader()
    
    # Записываем строки с данными учеников
    for student in students:
        writer.writerow(student)

print("Файл students.csv создан!")