import csv  # Модуль для работы с CSV

# Открываем файл для чтения ('r' — read)
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    
    # Проходим по каждой строке (каждому ученику)
    for student in reader:
        print(f"Имя: {student['name']}, Возраст: {student['age']}, Оценка: {student['grade']}")