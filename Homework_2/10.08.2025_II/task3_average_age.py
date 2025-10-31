import csv

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    
    total_age = 0  # Сумма возрастов
    count = 0      # Количество учеников
    
    for student in reader:
        age = int(student["age"])  # Преобразуем возраст в число
        total_age += age
        count += 1

if count > 0:
    average_age = total_age / count
    print(f"Средний возраст учеников: {average_age:.2f}")
else:
    print("Нет данных для подсчёта.")
