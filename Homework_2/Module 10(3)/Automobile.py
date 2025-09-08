class Avtomobil:
    def __init__(self, model, year, manufacturer, engine_volume, color, price):
        self.model = model                   # Название модели
        self.year = year                     # Год выпуска
        self.manufacturer = manufacturer     # Производитель
        self.engine_volume = engine_volume   # Объем двигателя
        self.color = color                   # Цвет машины
        self.price = price                   # Цена

    def input_data(self):
        """Метод для ввода данных об автомобиле."""
        self.model = input("Введите название модели: ")
        self.year = int(input("Введите год выпуска: "))
        self.manufacturer = input("Введите производителя: ")
        self.engine_volume = float(input("Введите объем двигателя: "))
        self.color = input("Введите цвет машины: ")
        self.price = float(input("Введите цену: "))

    def output_data(self):
        """Метод для вывода данных об автомобиле."""
        print(f"Модель: {self.model}")
        print(f"Год выпуска: {self.year}")
        print(f"Производитель: {self.manufacturer}")
        print(f"Объем двигателя: {self.engine_volume}L")
        print(f"Цвет: {self.color}")
        print(f"Цена: {self.price} рублей")

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_manufacturer(self):
        return self.manufacturer

    def get_engine_volume(self):
        return self.engine_volume

    def get_color(self):
        return self.color

    def get_price(self):
        return self.price
    
    def display_info(self):
        return f"Модель: {self.model}, Год: {self.year}, Цвет: {self.color}"
    
# Ввод данных о машине
my_car = Avtomobil("Porshe", 2000, "Germany", 3.0, "Black", 50.000)
my_car.input_data()

# Вывод данных о машине
my_car.output_data()

# Получение доступа к отдельным полям
print(f"Модель автомобиля: {my_car.get_model()}")

print(f"Модель автомобиля: {my_car.get_model()}")
print(f"Год выпуска: {my_car.get_year()}")
print(f"Цвет: {my_car.get_color()}")

# Вывод дополнительной информации
print(my_car.display_info())