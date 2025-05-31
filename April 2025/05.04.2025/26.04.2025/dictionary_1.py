capitals = {"Russia": "Moscow", "Great Britan": "London", "Spain": "Madrid"}
print(capitals)
print(f"Столица России является {capitals['Russia']}")

capitals = dict(Russia="Moscow", Great_Britan="London", Spain="Madrid") # создание словаря через встроенную функцию
print(capitals)

capitals = dict([("Russia","Moscow"), ("Great Britan","London"), ("Spain","Madrid")])# Вариант списка кортежей
print(capitals)

for i in capitals: # По стандарту эта запись выводит нам ключи(Russia, Great Britany, Spain)
    print(i)

for key in capitals: # Выводим значение(Moscow, London, Madrid)
    print(capitals[key])

for key in capitals: # Выводим значение "Russia" "Moscow"
    print(key, capitals [key])  

    # Метод keys(Ключи)

for key in capitals.keys():
    print(key)

    # Метод - values(значения). Выведем значения(value)
for value in capitals.values():
    print(value)

# Метод -  вывод пар ключ значение
for item in capitals.items():
    print(item)

# распаковка кортежей(ключ, значение)
for key, value in capitals.items():
    print(key, value)

capitals = {0:"Moscow", 1: "London", 2: "Madrid"} 
print(capitals[0])