ls1 = input("Введите список целых чисел через пробел")
print(ls1)
ls1 = ls1.split()
print(ls1)

for i in range(len(ls1)):
    ls1[i] = int(ls1[i])

print(ls1)

# ls1 = [1, 22, -12, -4, -27, 5, 108, 45, 34, 98]
#Сумма отрицательных чисел
# s = 0
# for i in ls1:
    # if i < 0:
        # s += i
# print(s)