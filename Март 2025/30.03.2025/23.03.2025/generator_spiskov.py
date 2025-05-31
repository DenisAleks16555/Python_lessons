#генератор списков
# a = input("Введите список целых чисел через пробел")
# ls1 = [int(i) for i in a.split()]
# print(ls1)

# нужно получить 10 нулей
# ls0 = [0 for i in range(10)]
# print(ls0)

# Найти сумму отрицательных чисел
a = input("Введите список целых чисел через пробел")
ls1 = sum([int(i) for i in a.split() if int(i) < 0]) 
# ls1 = ([int(i) for i in a.split() if int(i) < 0]) 
#ls1 = sum(ls1)
print(ls1)

# Без генератора как выглядит
ls1 = []
for i in a.split():
    if int(i) < 0:
        ls1.append(int(i))
ls1 = sum(ls1)
print(ls1)
