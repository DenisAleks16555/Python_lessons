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

    def display_data(self, show_year=True):
        """Метод для вывода данных об автомобиле."""
        print(f"Модель: {self.model}")
        print(f"Производитель: {self.manufacturer}")
        print(f"Объем двигателя: {self.engine_volume}L")
        print(f"Цвет: {self.color}")
        print(f"Цена: {self.price} рублей")
        if show_year:
            print(f"Год выпуска: {self.year}")

# Создаём объект автомобиля через конструктор
avtomobil = Avtomobil("Porshe", 2000, "Germany", 3.0, "Black", 50.000)

# Выводим данные автомобиля
avtomobil.display_data()  # Показывает все данные
avtomobil.display_data(show_year=False)  # Показывает данные без Года выпуска 