import sqlite3  # Это подключает библиотеку для работы с базой данных

# Шаг 1: Подключаемся к базе данных (если файла нет, он создастся)
conn = sqlite3.connect('cinema.db')
cursor = conn.cursor()  # Это как "указатель" для выполнения команд в базе

# Шаг 2: Создаём таблицы
cursor.execute('''
CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY,
    title TEXT,
    genre TEXT,
    duration INTEGER
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS halls (
    id INTEGER PRIMARY KEY,
    name TEXT,
    capacity INTEGER
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS sessions (
    id INTEGER PRIMARY KEY,
    movie_id INTEGER,
    hall_id INTEGER,
    start_time TEXT,
    FOREIGN KEY (movie_id) REFERENCES movies (id),
    FOREIGN KEY (hall_id) REFERENCES halls (id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS tickets (
    id INTEGER PRIMARY KEY,
    session_id INTEGER,
    buyer_name TEXT,
    price INTEGER,
    FOREIGN KEY (session_id) REFERENCES sessions (id)
)
''')

# Шаг 3: Вставляем данные в таблицы
# Данные для movies
movies_data = [
    (1, 'Интерстеллар', 'фантастика', 169),
    (2, 'Начало', 'боевик', 148),
    (3, 'Матрица', 'фантастика', 136),
    (4, 'Джокер', 'драма', 122),
    (5, 'Паразиты', 'триллер', 132),
    (6, 'Зелёная книга', 'драма', 130),
    (7, 'Безумный Макс: Дорога ярости', 'боевик', 120),
    (8, 'Гран Торино', 'драма', 116),
    (9, 'Дюна', 'фантастика', 155),
    (10, 'Варкрафт', 'фэнтези', 123)
]
cursor.executemany('INSERT INTO movies VALUES (?, ?, ?, ?)', movies_data)

# Данные для halls
halls_data = [
    (1, 'Зал 1', 100),
    (2, 'Зал 2', 80),
    (3, 'Зал 3', 50),
    (4, 'Зал 4', 120),
    (5, 'Зал 5', 60),
    (6, 'Зал 6', 90),
    (7, 'VIP 1', 30),
    (8, 'VIP 2', 25),
    (9, 'IMAX', 200),
    (10, '4DX', 110)
]
cursor.executemany('INSERT INTO halls VALUES (?, ?, ?)', halls_data)

# Данные для sessions
sessions_data = [
    (1, 1, 1, '2025-09-01 18:00'),
    (2, 2, 2, '2025-09-01 20:00'),
    (3, 3, 3, '2025-09-02 19:00'),
    (4, 4, 4, '2025-09-02 21:30'),
    (5, 5, 5, '2025-09-03 18:15'),
    (6, 6, 6, '2025-09-03 19:00'),
    (7, 7, 7, '2025-09-03 21:00'),
    (8, 8, 8, '2025-09-04 17:45'),
    (9, 9, 9, '2025-09-04 20:10'),
    (10, 10, 10, '2025-09-05 19:40')
]
cursor.executemany('INSERT INTO sessions VALUES (?, ?, ?, ?)', sessions_data)

# Данные для tickets
tickets_data = [
    (1, 1, 'Иванов Иван', 500),
    (2, 2, 'Петров Пётр', 450),
    (3, 3, 'Сидоров Сидор', 500),
    (4, 4, 'Смирнова Мария', 400),
    (5, 5, 'Петрова Анна', 550),
    (6, 6, 'Кузнецов Алексей', 480),
    (7, 7, 'Васильева Ольга', 600),
    (8, 8, 'Орлов Дмитрий', 420),
    (9, 9, 'Миронова Екатерина', 650),
    (10, 10, 'Соколов Андрей', 700)
]
cursor.executemany('INSERT INTO tickets VALUES (?, ?, ?, ?)', tickets_data)

# Сохраняем изменения
conn.commit()

# Шаг 4: Выполняем задания (запросы)
print("Задача 1: Список проданных билетов с фильмом, залом и покупателем")
query1 = '''
SELECT movies.title, halls.name, tickets.buyer_name
FROM tickets
JOIN sessions ON tickets.session_id = sessions.id
JOIN movies ON sessions.movie_id = movies.id
JOIN halls ON sessions.hall_id = halls.id
'''
cursor.execute(query1)
results1 = cursor.fetchall()
for row in results1:
    print(row)

print("\nЗадача 2: Количество билетов по каждому фильму")
query2 = '''
SELECT movies.title, COUNT(tickets.id) AS ticket_count
FROM tickets
JOIN sessions ON tickets.session_id = sessions.id
JOIN movies ON sessions.movie_id = movies.id
GROUP BY movies.title
'''
cursor.execute(query2)
results2 = cursor.fetchall()
for row in results2:
    print(row)

print("\nЗадача 3: Суммарная выручка по всем билетам")
query3 = '''
SELECT SUM(price) AS total_revenue
FROM tickets
'''
cursor.execute(query3)
result3 = cursor.fetchone()
print(f"Общая выручка: {result3[0]} рублей")

# Закрываем соединение
conn.close()
