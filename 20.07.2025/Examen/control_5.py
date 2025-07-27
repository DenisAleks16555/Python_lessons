# Задание 5: Фабрика Героев (10 минут)
# Цель: Проверить понимание статических и классовых методов.

# Добавьте в класс Hero статический метод show_rules(), который просто выводит строку "Правила игры: побеждает тот, кто остался жив.". Он не принимает никаких аргументов, кроме self или cls.
# Добавьте в класс Hero метод класса (@classmethod) с именем create_warrior(). Этот метод должен создавать и возвращать экземпляр класса Hero с именем "Воин" и здоровьем 110.
# Добавьте аналогичный метод класса create_mage(), который создает героя с именем "Маг" и здоровьем 80.
# Пример использования:

# Hero.show_rules() # Вызов статического метода
# warrior = Hero.create_warrior()
# mage = Hero.create_mage()
# print(warrior)
# print(mage)

# Ожидаемый результат:
# Правила игры: побеждает тот, кто остался жив.
# Герой Воин, Здоровье: 110
# Герой Маг, Здоровье: 80

class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def __str__(self):
        return f"Герой {self.name}, Здоровье: {self.health}"

    @staticmethod

    def show_rules():
        print("Правила игры: побеждает тот, кто остался жив")



    @classmethod
    def create_warrior(cls):
        return cls("Воин",110)

    @classmethod
    def create_mage(cls):
        return cls("Маг",80)
    
Hero.show_rules()  # Выводит правила
warrior = Hero.create_warrior()
mage = Hero.create_mage()
print(warrior)
print(mage)


