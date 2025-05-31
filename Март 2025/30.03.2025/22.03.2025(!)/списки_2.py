ls = [12, 22, 44, 54,9]
lsf = [0, 0, 7]

print(len(ls))
print(max(ls))
print(min(ls))
print(sum(ls))
print(sorted(ls)) #Сортирует 
print(sorted(ls,reverse=True)) # Сортирует от большего к меньшему 

print(ls + lsf)
print(ls * 2)

# Методы списка
# Добавление значения в список
ls.append(55)
ls.append(lsf)
print(ls[-1] [2])
#Добавить под каким-то индексом
print(ls)
ls.insert(1, 123)
print(ls)

# ls.remove("привет")
# ls.remove("привет")
# print(ls)

# ls.remove("привет")
print(ls)
x = ls.pop()
print(x)
print(ls)
ls.pop(4)
print(ls)

ls.append(22)
print(ls)
print(ls.index(22))

print(ls.count(22))

ls.sort()
print(ls)
# переворачивает наш список с права на лево
ls.reverse()
print(ls)

#Очищает полностью список
# ls.clear()
# print(ls)

# оператор принадлежности in
print(ls)
print(55 in ls)
print(100 in ls)

ls = []
ls = [1, 3, 4]
ls = list()

s = "Мама мыла раму"
ls = list(s)
print(ls)
ls = s.split()
print(ls)
l = "Яблоко,персик,банан"
ls = l.split(",")
print(ls)


