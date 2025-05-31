# Подсчёт символов в строке

s = input("Введите любой текст: ")
dct = {}

# Hello
for ch in s.split():# s.split Считаем каждое слово 
    dct[ch] = dct.get(ch, 0) + 1
print(dct)

