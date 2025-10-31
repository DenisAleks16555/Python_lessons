import sqlite3

# Функция для автоматического сохранения в файлы (с правильной кодировкой UTF-8)
def save_to_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as f:
        if isinstance(content, list):
            # Список кортежей — выводим построчно
            for row in content:
                # Преобразуем каждый элемент строки в строку и соединяем табуляцией
                f.write('\t'.join(str(x) for x in row) + '\n')
        else:
            # Один элемент (например, число или кортеж)
            if isinstance(content, tuple):
                f.write('\t'.join(str(x) for x in content) + '\n')
            else:
                f.write(str(content) + '\n')
                
# Создание новой базы (my_new_db.db) и подключение
conn = sqlite3.connect('my_new_db.db')
cursor = conn.cursor()

# Удаляем таблицы, если они существуют (чтобы пересоздать с правильной структурой)
cursor.execute('DROP TABLE IF EXISTS books')
cursor.execute('DROP TABLE IF EXISTS orders')

# Создание таблиц с правильными столбцами
cursor.execute('''CREATE TABLE books (
    id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT,
    price REAL,
    quantity INTEGER
)''')

cursor.execute('''CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    book_id INTEGER,
    quantity INTEGER,
    FOREIGN KEY (book_id) REFERENCES books (id)
)''')

# Вставка примерных данных (замени на свои из CSV, если нужно)
# Книги
cursor.execute("INSERT INTO books (title, author, price, quantity) VALUES (?, ?, ?, ?)", ('Книга1', 'Автор1', 100.0, 10))
cursor.execute("INSERT INTO books (title, author, price, quantity) VALUES (?, ?, ?, ?)", ('Книга2', 'Автор2', 200.0, 5))
cursor.execute("INSERT INTO books (title, author, price, quantity) VALUES (?, ?, ?, ?)", ('Евгений Онегин', 'А. С. Пушкин', 150.0, 10))
cursor.execute("INSERT INTO books (title, author, price, quantity) VALUES (?, ?, ?, ?)", ('Книга3', 'Автор3', 50.0, 20))

# Заказы (примеры)
cursor.execute("INSERT INTO orders (book_id, quantity) VALUES (?, ?)", (1, 5))  # Книга1
cursor.execute("INSERT INTO orders (book_id, quantity) VALUES (?, ?)", (2, 2))  # Книга2
cursor.execute("INSERT INTO orders (book_id, quantity) VALUES (?, ?)", (3, 10)) # Евгений Онегин

# Сохранение изменений
conn.commit()

# Запросы и сохранение результатов в файлы

# Запрос 1: Названия и цены книг, которые заказывали
cursor.execute('''
    SELECT b.title, b.price
    FROM books b
    JOIN orders o ON b.id = o.book_id
''')
result1 = cursor.fetchall()
save_to_file('result1.txt', result1)

# Запрос 2: Названия и цены книг, которые НЕ заказывали
cursor.execute('''
    SELECT b.title, b.price
    FROM books b
    LEFT JOIN orders o ON b.id = o.book_id
    WHERE o.id IS NULL
''')
result2 = cursor.fetchall()
save_to_file('result2.txt', result2)

# Запрос 3: Стоимость всех книг Пушкина на складе
cursor.execute('''
    SELECT SUM(b.price * b.quantity)
    FROM books b
    WHERE b.author = 'А. С. Пушкин'
''')
result3 = cursor.fetchone()[0]
save_to_file('result3.txt', result3)

# Запрос 4: Самая дорогая проданная книга (название и цена)
cursor.execute('''
    SELECT b.title, b.price
    FROM books b
    JOIN orders o ON b.id = o.book_id
    ORDER BY b.price DESC
    LIMIT 1
''')
result4 = cursor.fetchone()
save_to_file('result4.txt', result4)

# Запрос 5: Количество заказов по авторам
cursor.execute('''
    SELECT b.author, SUM(o.quantity) as total_orders
    FROM books b
    JOIN orders o ON b.id = o.book_id
    GROUP BY b.author
    ORDER BY total_orders DESC
''')
result5 = cursor.fetchall()
save_to_file('result5.txt', result5)

# Закрытие соединения
conn.close()

print("База создана, данные вставлены, результаты сохранены в result1.txt - result5.txt")
