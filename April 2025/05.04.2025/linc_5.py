def is_simple_number(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

lst = [23, 7, 1344, 4, 45874, 9998974, 75664654, 4566]
lst_2 = list(map(is_simple_number, lst))
print(lst_2)