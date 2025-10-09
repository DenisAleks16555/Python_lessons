from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime
from flask import jsonify

app = Flask(__name__)
DATABASE = 'budget.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Инициализация базы данных при запуске
def init_db():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        # Создаем таблицу, если еще не существует
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            amount REAL NOT NULL,
            date TEXT NOT NULL
        )
        ''')
        # Проверка и добавление начальных данных (если их еще нет)
        cursor.execute('SELECT COUNT(*) FROM expenses')
        count = cursor.fetchone()[0]
        if count == 0:
            cursor.execute("INSERT INTO expenses (description, amount, date) VALUES (?, ?, ?)",
                           ('Покупка продуктов', 5000, '2025-09-10'))
            cursor.execute("INSERT INTO expenses (description, amount, date) VALUES (?, ?, ?)",
                           ('Такси', 1200, '2025-09-10'))
        conn.commit()

@app.route('/expenses')
def get_expenses():
    conn = get_db_connection()
    expenses = conn.execute('SELECT * FROM expenses').fetchall()
    conn.close()
    # преобразуем расходы в список словарей
    expenses_list = [dict(expense) for expense in expenses]
    return jsonify(expenses_list)

@app.route('/')
def index():
    conn = get_db_connection()
    expenses = conn.execute('SELECT * FROM expenses').fetchall()
    conn.close()
    # cursor = conn.cursor()
    # expenses = cursor.execute("SELECT * FROM expenses").fetchall()
    # total = sum([expense['amount'] for expense in expenses])
    return render_template('index.html', expenses=expenses) 
# , total=total)

@app.route('/add', methods=('GET', 'POST'))
def add_expense():
    if request.method == 'POST':
        description = request.form['description']
        amount = float(request.form['amount'])
        date = request.form['date']
        conn = get_db_connection()
        # c = conn.cursor()
        conn.execute('INSERT INTO expenses (description, amount, date) VALUES (?, ?, ?)',
                  (description, amount, date))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add_expense.html')

@app.route('/delete/<int:expense_id>', methods=['POST'])
def delete_expense(expense_id):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('DELETE FROM expenses WHERE id=?', (expense_id,))
    conn.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

# //127.0.0.1:5000/
# Сделать сайт удобным для мобильных устройств
# Сделать так, чтобы сайт хорошо выглядел и работал на телефонах и планшетах. Это называется адаптивный дизайн.












# @app.route('/delete/<int:expense_id>', methods=['POST'])
# def delete_expense(expense_id):
#     conn = get_db()
#     cursor = conn.cursor()
#     cursor.execute("DELETE FROM expenses WHERE expense_id = ?", (expense_id,))
#     conn.commit()
#     return redirect(url_for('index'))

# if __name__ == '__main__':
#     init_db()  # Инициализируем базу данных при запуске
#     app.run(debug=True)
   
# init_db()

# # Главная страница - список расходов и итог
# @app.route('/')
# def index():
#     conn = sqlite3.connect('budget.db')
#     c = conn.cursor()
#     c.execute('SELECT * FROM expenses')
#     expenses = c.fetchall()
#     total = sum([expense[2] for expense in expenses])  # сумма по полю amount
#     conn.close()
#     return render_template('index.html', expenses=expenses, total=total)

# # Страница для добавления расхода (форма)
# @app.route('/add', methods=['GET', 'POST'])
# def add_expense():
#     if request.method == 'POST':
#         description = request.form['description']
#         amount = float(request.form['amount'])
#         date = request.form['date']
#         conn = sqlite3.connect('budget.db')
#         c = conn.cursor()
#         c.execute('INSERT INTO expenses (description, amount, date) VALUES (?, ?, ?)',
#                   (description, amount, date))
#         conn.commit()
#         conn.close()
#         return redirect(url_for('index'))
#     return render_template('add_expense.html')

# from flask import redirect, url_for

# @app.route('/delete/<int:expense_id>', methods=['POST'])
# def delete_expense(expense_id):
#     # тут нужно написать код удаления из базы данных
#     # например:
#     # db.execute('DELETE FROM expenses WHERE id=?', (expense_id,))
#     # или, если используете SQLAlchemy:
#     # expense = Expense.query.get(expense_id)
#     # db.session.delete(expense)
#     # db.session.commit()
#     conn = sqlite3.connect('budget.db')
#     c = conn.cursor()
#     c.execute('DELETE FROM expenses WHERE id=?', (expense_id,))
#     conn.commit()
#     conn.close()
#     # После удаления перенаправим обратно на страницу с расходами
#     return redirect(url_for('index'))

# if __name__ == '__main__':
#     app.run(debug=True)
