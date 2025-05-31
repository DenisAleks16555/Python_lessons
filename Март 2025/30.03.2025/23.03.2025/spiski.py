ls1 = [1, 22, -12, -4, -27, 5, 108, 45, 34, 98]
#Сумма отрицательных чисел
s = 0
for i in ls1:
    if i < 0:
        s += i
print(s)
#Сумма чётных чисел
s = 0 
for i in ls1:
    if i % 2 == 0:
        s += i 
print(s)

# Сумма нечётных чисел
s = 0 
for i in ls1:
    if i % 2 != 0:
        s += i 
print(s)
 #Произведение элементов с индексами кратными 3
j = 1
for i in range(len(ls1)):
    if i % 3 == 0:
        j *= ls1[i]
        
print(j)

# Произведение элементов между максимальным и минимальным элементом
ls1 = [1, 22, - 12, -4, -27, 5, 108, 45, 34, 98]
ls1_max = max(ls1)
ls1_min = min(ls1)
print(ls1_max * ls1_min)

a = (ls1.index(ls1_min))
b = (ls1.index(ls1_max))
ls2 = ls1[a:b]

#Сумму элементов, находящихся между первым и последним положительным элементом.
s = 0
for i in range(len(ls1)):
        if ls1[i] > 0:
         s = i # нашли первый элемент
        break
v = 0
for i in range(len(ls1)):
        if ls1[i] > 0:
         v = i # нашли первый элемент
      
ls3 = ls1[s + 1 :v]
print(sum(ls3))

