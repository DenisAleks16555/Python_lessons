class Flat:
    def __init__(self, area, price):
        self.area = area  # Площадь квартиры
        self.price = price  # Цена квартиры

    def __str__(self):
        return f"Квартира: Площадь = {self.area} м², Цена = {self.price} руб."
    

    def __eq__(self, other):
        return self.area == other.area

    def __ne__(self, other):
        return self.area != other.area

    def __gt__(self, other):
        return self.price > other.price

    def __lt__(self, other):
        return self.price < other.price

    def __ge__(self, other):
        return self.price >= other.price

    def __le__(self, other):
        return self.price <= other.price
    
# Создаем квартиры
flat1 = Flat(50, 3000000)  # Площадь 50 м², цена 3 000 000
flat2 = Flat(50, 3500000)  # Площадь 50 м², цена 3 500 000
    
# Выводим информацию о квартирах
print(flat1)  # Вывод информации о flat1
print(flat2)  # Вывод информации о flat2

# Проверяем на равенство площадей
print(flat1 == flat2)  # True, площади одинаковые

# Проверяем на неравенство площадей
print(flat1 != flat2)  # False, площади одинаковые

# Сравниваем по цене
print(flat1 < flat2)   # True, flat1 дешевле
print(flat1 > flat2)   # False, flat1 не дороже
print(flat1 <= flat2)  # True, flat1 не дороже
print(flat1 >= flat2)  # False, flat1 не дороже





