def sum_n(a,b):
    return a + b

print(sum_n(1,5))

# Тоже самое мы можем сделать с помощью класса
class Sum_c:
    def __init__(self, a, b):
        self.a = a
        self.b = b
# Метод из класса делать функцию
    def __call__(self, *args, **kwds):
        return self.a + self.b
    
s = Sum_c(1, 5)
print(s())


#print(callable(int)) # функция позволяет можно ли вызвать этот класс в виде функции