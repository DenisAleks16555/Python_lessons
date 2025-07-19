class Shape:
    def __init__(self):
        pass

   

class Rectangle(Shape):
    pass

class Triangle(Shape):
    pass

class Circle(Shape):
    pass

class Square(Rectangle):
    pass

class Iso_Triangle(Triangle):
    pass

class Equ_Triangle(Triangle):
    pass


print(issubclass(Square, Rectangle))
print(issubclass(Iso_Triangle, Triangle))
print(issubclass(Equ_Triangle, Triangle))
print(issubclass(Circle, Shape))
print(issubclass(Triangle, Shape))
print(issubclass(Rectangle, Shape))
