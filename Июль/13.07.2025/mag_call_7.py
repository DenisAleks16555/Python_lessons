class Car:
    def __init__(self, mark, color, year):
        self.mark = mark
        self.collor = color
        self.year = year

    def drive(self): # Метод экземпляра класса(экземпляр, т.е объект который может вызвать)Car.drive(car1)
        print("Машина поехала")

    @classmethod # Метод класса
    def description(cls):
    
        print("Это класс для создания автомобиля")
        print(cls)

    @classmethod
    def audi(cls, color, year):
        return cls("audi", color, year)
    
    @staticmethod
    def st():
        print("привет,это статический метод")

    def __str__(self):
        return f"Марка - {self.mark}\nцвет - { self.collor}\nГод выпуска - {self.year}"
    
car1 = Car("BMW", "black", 1981) 
car2 = Car.audi("White", 1950)
print(car1)
print()
print(car2)
car1.drive()

Car.description()

Car.st()
car1.st()




