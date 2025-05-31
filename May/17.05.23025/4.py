print("Введите любое число: ")

try:
    number = int(input())
    print(2 * number )
    print(2 / number )
    print(2 + number )
    print(2 - number )
    
except ValueError: # Блок ошибка значения
     print("Введены некорректные данные")
except ZeroDivisionError:  # Блок ошибка деления\ на 0
     print("Ошибка деления на ноль")

# print(number)