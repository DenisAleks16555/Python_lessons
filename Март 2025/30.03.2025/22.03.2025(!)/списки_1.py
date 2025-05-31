# ls = ["Петя", "Вася", "Коля", "Женя"]
# print(ls[0])

# name = ls[0]
# print(name)

# print(ls)
# ls[2] = "Света"
# print(ls)

# s = "Привет"
# print(s[0]) #Обращаемся к символу П(под индексом 0 у нас П)
# s[0] = "Б"
# print(s) # Ошибка. Строки нельзя перезаписывать 

# ls = [10, "Петя", 11.5, False]
# new_ls = ls
# new_ls[-1] = True
# print(ls)
# print(new_ls)


# ls = [10, "Петя", 11.5, False]
# new_ls = ls[:]
# new_ls[-1] = True
# print(ls)
# print(new_ls)

ls = [10, "Петя", 11.5, False]
print(ls)
new_ls = ls.copy()
new_ls[-1] = True
print(ls)
print(new_ls)

ls = [10, "Петя", 11.5, False]
print(type(ls)) # тип данных список

s = "Привет" # Преобразуем в список
ls = list(s)
print(ls)

#Метод собирает обратно в строку
print("".join(ls))
print("=".join(ls))


