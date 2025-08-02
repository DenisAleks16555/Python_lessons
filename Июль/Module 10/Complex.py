class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return Complex(real_part, imag_part)

    def __truediv__(self, other):
        denom = other.real**2 + other.imag**2
        real_num = self.real * other.real + self.imag * other.imag
        imag_num = self.imag * other.real - self.real * other.imag
        return Complex(real_num / denom, imag_num / denom)

    def __str__(self):
        # Форматируем вывод: например, "1 + 2i" или "3 - 4i"
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {-self.imag}i"
#Теперь, если создать комплексное число и вывести его:

# c = Complex(3, -4)
# print(c)  # Выведет: 3 - 4i

# Создаем два комплексных числа
c1 = Complex(1, 2)   # 1 + 2i
c2 = Complex(3, 4)   # 3 + 4i

# Складываем
result_add = c1 + c2
print(result_add)  # Выведет: 4 + 6i

# Вычитаем
result_sub = c1 - c2
print(result_sub)  # Выведет: -2 - 2i

# Умножаем
result_mul = c1 * c2
print(result_mul)  # Выведет: -5 + 10i

# Делим
result_div = c1 / c2
print(result_div)  # Выведет примерно: 0.44 + 0.08i