import sqlite3

connection = sqlite3.connect(r'23.08.2025\school.db')
cursor = connection.cursor()
print("База данных успешно подключена!")

cursor.execute("SELECT * FROM books") # метод выполнить какой-то запрос
rows = cursor.fetchall() # метод получить всё список кортежей получили строки
columns = [desc[0] for desc in cursor.description] # сформировали список из названия колонок

data = [dict(zip(columns,row)) for row in rows] # список словарей объдиняем слипляет названия со значениями


for d in data:
    print(d)

cursor.close()