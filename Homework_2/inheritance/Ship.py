class Ship:
    def __init__(self, name, manufacturer, power):
        self.name = name
        self.manufacturer = manufacturer
        self.power = power

    def get_info(self):
        return f"Корабль: {self.name}, Производитель: {self.manufacturer}, Мощность: {self.power}л.с."
    
class Frigate(Ship):
    def __init__(self, name, manufacturer, power, displacement):
        super().__init__(name, manufacturer, power)
        self.displacement = displacement
    def get_info(self):
        return f"Фригат: {self.name}, Производитель: {self.manufacturer}, Мощность: {self.power}л.с., Водоизмещение: {self.displacement} тонн полное."
    
class Destroyer(Ship):
    def __init__(self, name, manufacturer, power, cruising_range):
        super().__init__(name, manufacturer, power)
        self.cruising_range = cruising_range
    def get_info(self):
        return f"Эсминец: {self.name}, Производитель: {self.manufacturer}, Мощность: {self.power}, Дальность плавания: {self.cruising_range} морских миль."
    
class Cruiser(Ship):
    def __init__(self, name, manufacturer, power, cruiser_type):
        super().__init__(name, manufacturer, power)
        self.cruiser_type = cruiser_type
    def get_info(self):
        return f"Крейсер: {self.name}, Производитель: {self.manufacturer}, Мощность: {self.power}, Тип Крейсера: {self.cruiser_type}"
# Создаём объекты
ship = Ship("Gerald R.Ford", "USA", 350000)
frigate = Frigate("Garsia", "USA", 35000, 247)
destroyer = Destroyer("Flatcher", "USA", 60000, 2924)
cruiser = Cruiser("Boston", "USA", 120000, "Классический")

# Выводим информацию
print(ship.get_info())
print(frigate.get_info())
print(destroyer.get_info())
print(cruiser.get_info())
        
        