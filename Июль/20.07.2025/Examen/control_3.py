# Задание 3: Контроль над здоровьем (15 минут)
# Цель: Использовать свойства (@property, setter) для контроля над атрибутами.

# Измените класс Hero. Переименуйте атрибут health в _health (принятое соглашение для "защищенных" атрибутов).
# Создайте свойство (@property) с именем health, которое будет возвращать значение _health.
# Создайте сеттер для этого свойства (@health.setter). В сеттере добавьте логику:
# Если новое значение здоровья меньше или равно 0, атрибут _health должен становиться равным 0.
# В остальных случаях _health просто принимает новое значение.
# Добавьте новое свойство (только для чтения, без сеттера) is_alive, которое будет возвращать True, если здоровье героя больше 0, и False в противном случае.
# Пример использования (продолжение):
# hero2 = Hero("Гэндальф", 120)
# print(f"Жив ли {hero2.name}? {hero2.is_alive}")
# hero2.health = 50 # Используем сеттер
# print(hero2)
# hero2.take_damage(150) # Получает урон больше, чем есть здоровья
# print(hero2)
# print(f"Жив ли {hero2.name}? {hero2.is_alive}")

# Ожидаемый результат:
# Жив ли Гэндальф? True
# Герой Гэндальф, Здоровье: 50
# Гэндальф получил 150 урона. Осталось -100 здоровья.
# Герой Гэндальф, Здоровье: 0
# Жив ли Гэндальф? False

class Hero:
    def __init__(self, name, health):
        self.name = name
        self._health = health 

    @property
    def health(self):
        return self._health
    
    @health.setter
    def health(self, value):
        if value <=0:
            self._health = 0
        else:
            self._health = value

    @property
    def is_alive(self):
        return self._health > 0
    
    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} получил {amount} урона. Осталось {self.health} здоровья.")

    def __str__(self):
        return f"Герой {self.name}, Здоровье: {self.health}"
    
hero2 = Hero("Гэндальф", 120)
print(f"Жив ли {hero2.name}? {hero2.is_alive}")  # Проверяем текущий статус
hero2.take_damage(50)
print(hero2)
hero2.take_damage(150) # Получает урон больше,чем есть здоровья
print(hero2)
print(f"Жив ли {hero2.name}? {hero2.is_alive}")

