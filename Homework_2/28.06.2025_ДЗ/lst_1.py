def split_even_odd(lst):
    even_numbers = []  # Список для четных чисел
    odd_numbers = []   # Список для нечетных чисел
    
    for number in lst:
        if number % 2 == 0:  # Проверка на четность
            even_numbers.append(number)  # добавляем четное число в список
        else:
            odd_numbers.append(number)  # добавляем нечетное число в список
            
    return (even_numbers, odd_numbers)  # Возврат двух списков в кортеже

# Пример использования функции
input_list = [1, 2, 3, 4, 5, 6]
result = split_even_odd(input_list)
print(result)  # Вывод: ([2, 4, 6], [1, 3, 5])