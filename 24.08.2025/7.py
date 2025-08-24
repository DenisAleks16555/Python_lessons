import sqlite3

connection = sqlite3.connect(r'24.08.2025\school.db')
cursor = connection.cursor() # будут возвращаться словари

cursor.execute("SELECT * FROM wallets") # execut - управление
d = cursor.description # Здесь будет храниться системная информация о нашем запросе о наших колонках, храниться она списком

for i in d:
    print(i[0]) # С помощью этого мы можем получить имена колонок

name_list = [i[0] for i in d] 
print(name_list)



