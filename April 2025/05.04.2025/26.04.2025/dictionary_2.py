capitals = {"Russia": "Moscow", "Great Britan": "London", "Spain": "Madrid"}
capitals2 = {"Russia": "Moscow", "Great Britan": "London", "Spain": "Madrid"}

if "Russia" in capitals: # Проверяем есть ли ключ в словаре
    print(f"Столица России - {capitals['Russia']}")
    
    # Также можем сравнивать словари
print("Russia" in capitals) # Есть ли Россия в словаре( Выдаст True)
print(capitals == capitals2) # Выдаст True


# Проверяем есть ли строчка Москва в значениях нашего словаря
print("Moscow" in capitals.values())