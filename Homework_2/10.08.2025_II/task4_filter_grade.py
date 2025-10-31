import csv

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    
    print("Ученики с оценкой 'A':")
    for student in reader:
        if student["grade"] == "A":
            print(f"Имя: {student['name']}, Возраст: {student['age']}, Оценка: {student['grade']}")
