import sqlite3

# Без закрытия - используем With
with sqlite3.connect(r'24.08.2025\school.db') as connection:
    cursor = connection.cursor()
    cursor.execute('''
    SELECT author, COUNT(id)
    FROM books
    GROUP BY author
    ORDER BY COUNT(id) DESC                   
    ''')

rows = cursor.fetchall()
for row in rows:
    print(*row) # (* Чтобы убра все скобки,запятые)