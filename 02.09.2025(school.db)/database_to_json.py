import sqlite3
import json

# Подключаемся к базе
conn = sqlite3.connect('school.db')
cursor = conn.cursor()

# Выполняем запрос, например, выбираем все из таблицы students
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

# Получаем имена колонок
columns = [desc[0] for desc in cursor.description]

# Формируем список словарей (каждая строка — словарь {столбец: значение})
result = [dict(zip(columns, row)) for row in rows]

# Сохраняем в JSON файл
with open('students.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)

print("Экспорт завершён, файл students.json создан.")

# Закрываем соединение
conn.close()

