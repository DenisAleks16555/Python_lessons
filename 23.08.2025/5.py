import sqlite3

connection = sqlite3.connect(r'23.08.2025\school.db')
cursor = connection.cursor()
print("База данных успешно подключена!")

cursor.execute("SELECT * FROM workers") # метод выполнить какой-то запрос
rows = cursor.fetchall() # метод получить всё
columns = [desc[0] for desc in cursor.description]

print(columns)

cursor.close()