# Задание 4: Сравнение Героев (10 минут)
# Цель: Реализовать магические методы сравнения.

# В классе Hero реализуйте магические методы для сравнения героев по их текущему уровню здоровья (_health):
# __eq__(other) (равно, ==)
# __lt__(other) (меньше, <)
# __gt__(other) (больше, >)
# Пример использования (продолжение):

# hero1 = Hero("Арагорн", 100)
# hero2 = Hero("Гэндальф", 120)
# hero3 = Hero("Леголас", 100)
# print(hero1 == hero2)
# print(hero1 == hero3)
# print(hero1 < hero2)
# print(hero1 > hero2)

# Ожидаемый результат:
# False
# True
# True
# False

   

class Hero:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return f"Hero(name='{self.name}', level={self.level})"

    # Магический метод для равенства
    def __eq__(self, other):
        if isinstance(other, Hero):
            return self.level == other.level
        return NotImplemented

    # Магический метод для неравенства
    def __ne__(self, other):
        if isinstance(other, Hero):
            return self.level != other.level
        return NotImplemented

    # Магический метод для меньше
    def __lt__(self, other):
        if isinstance(other, Hero):
            return self.level < other.level
        return NotImplemented

    # Магический метод для больше
    def __gt__(self, other):
        if isinstance(other, Hero):
            return self.level > other.level
        return NotImplemented

    # Магический метод для меньше или равно
    def __le__(self, other):
        if isinstance(other, Hero):
            return self.level <= other.level
        return NotImplemented

    # Магический метод для больше или равно
    def __ge__(self, other):
        if isinstance(other, Hero):
            return self.level >= other.level
        return NotImplemented
    
hero1 = Hero("Арагорн",100)
hero2 = Hero("Гендольф",120)
hero3 = Hero("Легопас",100)
print(hero1 == hero2) # False,разные уровни - 100 и 120
print(hero1 == hero3) # True, уровни одинаковые 100 и 100
print(hero1 < hero2) # True, уровни - 100 и 120
print(hero1 > hero2) # False, уровни 100 и 120
