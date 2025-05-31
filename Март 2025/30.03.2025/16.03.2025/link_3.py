# s = input("Введите любую строку: ")
# chars = 0
# digits = 0
# for ch in s:
    # if ch.isalpha():
        # chars +=1
    # elif ch.isdigit():
    #  digits +=1
# print(f"Количество букв в строке: {chars}")
# print(f"Количество цифр в строке: {digits}")

s = input("Введите любую строку: ")
m= input("Введите слово которое нужно найти и заменить в строке: ")
n= input("Введите слово на на которое нужно  заменить: ")
print(s.replace(m, n))




# print(s.count(m)) # считает количество символов или слов( в данном случае точку)