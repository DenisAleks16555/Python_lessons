
file_name = input("Введите название файла для чтения: ")

try: 
    fl = open(file_name, "r", encoding="utf-8")
    print(fl.read())
    fl.close()
except:
    print("Файл не найден")

    