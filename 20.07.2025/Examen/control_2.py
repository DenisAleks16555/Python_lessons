# Задание 2: Первое действие (10 минут)
# Цель: Добавить метод экземпляра, который изменяет его состояние.

# В классе Hero из предыдущего задания создайте метод take_damage(damage).
# Этот метод должен принимать число damage (урон) и уменьшать на это значение атрибут health.
# После получения урона, метод должен выводить в консоль сообщение: "<Имя> получил <X> урона. Осталось <Y> здоровья.".
# Пример использования (продолжение):


# # hero1 создан в предыдущем задании

# hero1.take_damage(25)

# print(hero1) # Проверяем, что здоровье изменилось


# Ожидаемый результат:

# Арагорн получил 25 урона. Осталось 75 здоровья.

# Герой Арагорн, Здоровье: 75

class Hero:
    def __init__(self, damage, health):
        self.__damage = damage
        self.__health = health

    def take_damage(self,damage):
        self.health -= damage
        print(f"{self.name}получил{damage}урона.Осталось{self.health}здоровья.")

    def __str__(self):
        return f'Герой{self.name},Здоровье: {self.health}'
hero1 = Hero('Aragorn',100)
hero1.take_damage(25)
print(hero1)


