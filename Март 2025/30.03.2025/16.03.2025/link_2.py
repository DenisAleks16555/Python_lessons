#Срез строки

# s = "Тел. №89995553322 Семён"
# m = s [6:18]
# print(m)
# print(m[: : -1])
# s = input("Введите текст:")
# print(s[: : -1])

# s = "Anna"
# m = s[: : -1]
# print(s)
# print(m)
# print(s.lower() == m.lower())

user_name = "Viktor"
user_age = 54
user_height = 188

print("Кандитат на должность директора: \nИмя: " + user_name + " \nВозраст: " + str(user_age) + " \nРост: " + str(user_height))
print(f"Кандитат на должность директора: \nИмя:  {user_name}  \nВозраст:  {user_age}  \nРост:  {user_height}")
# (f) - Формирование строки