class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @property
    def perimetr(self):
        return (self.a + self.b + self.c) 
    
class Equ_Triangle(Triangle):
    def __init__(self, a):
        super().__init__(a, a, a)

fig1 = Triangle(2, 4, 8)
fig2 = Equ_Triangle(6)

print(fig1.perimetr)
print(fig2.perimetr)
