class Car:
    count = 0
    def __init__(self, name, power):
        Car.count +=1
        self.name = name
        self.power = power
        self.serial_number = Car.count

    def __str__(self):
        return f"Имя - {self.name}\nМощность - {self.power}\nКолличество созданных машин - {self.count}\nСерийный номер - {self.serial_number}"
    
car1 = Car("Tesla", 500)
print(car1)
car2 = Car("Mersedes", 350)
print(car2)
car3 = Car("BMW", 250)
print(car3)
car4 = Car("Audi", 200)
print(car4)

# Car.count = 999

# print(car1)
# print(car2)