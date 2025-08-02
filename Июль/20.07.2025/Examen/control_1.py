# Задание 1: Рождение Героя (10 минут)
# Цель: Создать базовый класс с конструктором и строковым представлением.

# Создайте класс Hero.
# При создании экземпляра (hero = Hero(...)) в него должны передаваться name (имя) и health (здоровье). Сохраните их как атрибуты экземпляра.
# Реализуйте магический метод __str__, который будет возвращать строку в формате "Герой <Имя>, Здоровье: <X>".
# Пример использования:

# hero1 = Hero("Арагорн", 100)

# print(hero1)


# Ожидаемый результат:

# Герой Арагорн, Здоровье: 100 

class Hero:
    def __init__(self, name, health):
        self.__name = name
        self.__health = health

    def name(self):
      return  self.__name
    
    def health(self):
       return self.__health
    def __str__(self):
       return f"name - {self.name}\nhealth - {self.health}"   


hero1  = ("Герой Aragorn", 100)
print(hero1)

