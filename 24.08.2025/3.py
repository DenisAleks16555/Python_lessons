import sqlite3

connection = sqlite3.connect(r'24.08.2025\school.db')
cursor = connection.cursor() # будут возвращаться словари

cursor.execute('''
               INSERT INTO books (title, author, publish_date, page_value)") # execut - управление
               VALUES ('Кубок огня', 'Джоан Роулинг', '2025-12-12', 650)
''')

print(cursor.lastrowid) # мы можем узнать последний id добавленной последней строки
connection.rollback() # отмена операции
connection.close() # Закрывает полностью базу данных




