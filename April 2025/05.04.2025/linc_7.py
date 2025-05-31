# Функция высшего порядка - Lambda(анонимная функция)
# def divide_by_2(number):
    # return number / 2

# lst = [34, 5657, 7748, 377]
# lst = list(map(divide_by_2, lst))
# print(lst)

#Lambda number: number / 2 Анонимная функция

lst = [34, 5657, 7748, 377]
lst = list(map(lambda number: number / 2, lst))
print(lst)

my_func = lambda number: number / 2
#my_func = lambda x: x/2 Сократили предыдущую строку
print(my_func(1200))