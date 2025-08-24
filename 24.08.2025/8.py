import sqlite3

connection = sqlite3.connect(r'24.08.2025\school.db')
cursor = connection.cursor() # будут возвращаться словари

new_wallets = [
   (1, 100),
   (2, 100),
   (3, 100),
]
cursor.executemany('''
               INSERT INTO wallets ('teacher_id', 'balance')
               VALUES (?, ?)
''', new_wallets)

cursor.execute("SELECT * FROM wallets") # метод выполнить какой-то запрос
rows = cursor.fetchall() # метод получить всё
for row in rows:
    print(row)

cursor.close()





