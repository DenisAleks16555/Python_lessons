# Таблица - walet
# Поля 
# id, 
# teacher_id связь с таблицей teachers
#  balance - число не может быть меньше 0
#  is_active - булевое значение

import sqlite3

connection = sqlite3.connect(r'24.08.2025\school.db')
cursor = connection.cursor() # будут возвращаться словари

cursor.execute('PRAGMA foreign_keys = ON')
      
            
  
cursor.execute('''
CREATE TABLE IF NOT EXISTS wallets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,    
    teacher_id INTEGER NOT NULL,
    balance INTEGER NOT NULL CHECK(balance >= 0),
    is_active INTEGER NOT NULL DEFAULT 1 CHECK(is_active IN (0, 1)),
    FOREIGN KEY (teacher_id) REFERENCES teachers (id))
    ''')
                    
               

connection.commit()
               




             