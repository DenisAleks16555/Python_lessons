import sys

fl = open("_input.txt", "r", encoding="utf-8")
sys.stdin = fl

try: # Пытаемся сделать вот это
    name = input()
    while name != '':
        print(f"Привет, {name}!")
        name = input()
except: # Исключая ошибки если будет ошибка то завершаем
    pass

fl.close()