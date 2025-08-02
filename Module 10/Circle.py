import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.circumference() < other.circumference()

    def __le__(self, other):
        return self.circumference() <= other.circumference()

    def __gt__(self, other):
        return self.circumference() > other.circumference()

    def __ge__(self, other):
        return self.circumference() >= other.circumference()
    
# Изменение радиуса
    def __iadd__(self, value):# Метод += позволяет увеличивать радиус окружности
        self.radius += value
        return self

    def __isub__(self, value):# Метод позволяет уменьшить радиус окружности
        self.radius -= value
        return self
# Метод circumference - длина окружности
    def circumference(self):
        return 2 * math.pi * self.radius #Вычисляет длину окружности по формуле:2*Pi*радиус
    
    def __str__(self):
        return f"Circle with radius {self.radius}"

# Пример использования:
c1 = Circle(5)
c2 = Circle(7)

print(c1 == c2)  # False
print(c1 < c2)   # True
c1 += 2
print(c1)        # Circle with radius 7