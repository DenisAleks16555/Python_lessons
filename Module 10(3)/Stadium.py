class Stadium:
    def __init__(self, name, opening_date, country, city, capacity):
        
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def input_data(self):
        """Метод для ввода данных о стадионе."""
        self.name = input("Введите название стадиона: ")
        self.opening_date = int(input("Введите дату открытия: "))
        self.country = input("Введите страну: ")
        self.city = input("Введите город: ")
        self.capacity = float(input("Введите вместимость: "))
        

    def display_data(self):
        """Метод для вывода данных о стадионе."""
        print(f"Название: {self.name}")
        print(f"Год открытия: {self.opening_date}")
        print(f"Страна: {self.country}")
        print(f"Город: {self.city}")
        print(f"Вместимость: {self.capacity}")
        

    def get_name(self):
        """Метод для получения названия стадиона."""
        return self.name

    def get_country(self):
        """Метод для получения страны."""
        return self.country

# Пример использования класса Stadium
stadium = Stadium("", 0, "", "", 0.0)  # Создаем объект стадиона с пустыми полями
stadium.input_data()                    # Заполняем данные стадиона с помощью метода
stadium.display_data()                  # Выводим данные стадиона


stadium = Stadium("Michigan", 1927, "USA", "Ann-Arbor", 107000)

stadium.input_data()