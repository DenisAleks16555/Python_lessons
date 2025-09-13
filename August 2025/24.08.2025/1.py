import sqlite3

connection = sqlite3.connect(r'24.08.2025\school.db')
connection.row_factory = sqlite3.Row # приходят кортежи ключ значения
cursor = connection.cursor()

cursor.execute("SELECT * FROM books") # execut - управление
rows = cursor.fetchall()
data = [dict(row) for row in rows]

# for d in data: (выводим как список словарей)
#     print(d)

for row in rows:
    print(row)  # Можем обращаться по индексу print(row[0]) или по названию print(row['title'])

cursor.close()