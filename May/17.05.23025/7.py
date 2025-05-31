# Управление ошибками
s = open("1.txt", "w", encoding="utf-8")

s.write("Добрый вечер Дамы и господа")
try:
    print(s.read())
   
except Exception as e:
    print(e)
finally: # Блок не обязателен, закрытие файла, сесии
    s.close()
    print("файл закрыт") 
