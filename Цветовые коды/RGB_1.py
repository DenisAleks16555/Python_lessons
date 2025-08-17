class ColorRGB:
    def __init__(self, r, g, b):
        # Можно добавить проверки диапазона (0-255), чтобы было безопаснее
        if not (0 <= r <= 255):
            raise ValueError("r должен быть в диапазоне 0-255")
        if not (0 <= g <= 255):
            raise ValueError("g должен быть в диапазоне 0-255")
        if not (0 <= b <= 255):
            raise ValueError("b должен быть в диапазоне 0-255")
        self.r = r
        self.g = g
        self.b = b

    def __str__(self):
        return f'#{self.r:02X}{self.g:02X}{self.b:02X}'

    def __repr__(self):
        return f'ColorRGB({self.r}, {self.g}, {self.b})'

    def __eq__(self, other):
        if isinstance(other, ColorRGB):
            return (self.r == other.r and self.g == other.g and self.b == other.b)
        return False
#Пример использования:
 
color1 = ColorRGB(255, 0, 0)
color2 = ColorRGB(255, 0, 0)
color3 = ColorRGB(0, 255, 0)

print(color1)            # #FF0000
print(repr(color1))      # ColorRGB(255, 0, 0)
print(color1 == color2)  # True
print(color1 == color3)  # False