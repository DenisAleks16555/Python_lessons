class Rectangle:
    def __init__(self, width, height):
        # Здесь мы сразу устанавливаем ширину и высоту через сеттеры,
        # чтобы сразу проверить, что они положительные
        self.width = width
        self.height = height

    # Геттер для width — возвращает значение ширины
    @property
    def width(self):
        return self._width

    # Сеттер для width — проверяет, что значение положительное
    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            print("Значение должно быть положительным")

    # Геттер для height — возвращает значение высоты
    @property
    def height(self):
        return self._height

    # Сеттер для height — проверяет, что значение положительное
    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            print("Значение должно быть положительным")

    # Свойство area — площадь, только для чтения (нет сеттера)
    @property
    def area(self):
        return self._width * self._height

    # Свойство perimeter — периметр, только для чтения
    @property
    def perimeter(self):
        return 2 * (self._width + self._height)

r = Rectangle(3, 4)
print(r.area)  # Выводит 12 (3 * 4)
print(r.perimeter)  # Выводит 14 (2*(3 + 4))

r.width = -5  # Попытка установить отрицательное значение. 
# Выведет: Значение должно быть положительным

r.height = 10  # Устанавливаем новую высоту
print(r.area)  # Теперь площадь 3 * 10 = 30
