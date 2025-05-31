#Функция высшего порядка - map

numbers = input()
print(numbers)
lst = numbers.split()
print(lst)
for i in range(len(lst)):
    lst[i] = int(lst[i])
print(lst)

lst_2 =  list(map(int, input().spl))
print(lst_2)