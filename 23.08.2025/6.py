import sqlite3

connection = sqlite3.connect(r'23.08.2025\school.db')
cursor = connection.cursor()
print("База данных успешно подключена!")

new_worker = ("Павел", 55, "сварщик")
cursor.execute('''
INSERT INTO workers (name, age, profesion)
VALUES (?, ?, ?)
               
''', new_worker)

connection.commit()

cursor.execute("SELECT * FROM workers") # метод выполнить какой-то запрос
rows = cursor.fetchall() # метод получить всё
for row in rows:
    print(row)

cursor.close()
