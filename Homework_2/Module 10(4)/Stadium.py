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
        

    def display_data(self, show_city=True):
        """Метод для вывода данных о стадионе."""
        print(f"Название: {self.name}")
        print(f"Год открытия: {self.opening_date}")
        print(f"Страна: {self.country}")
        print(f"Вместимость: {self.capacity}")
        if show_city:
            print(f"Город: {self.city}")       

   
# Создаём объект Стадион через конструктор
stadium = Stadium("Michigan", 1927, "USA", "Ann-Arbor", 107000)  
stadium.display_data()  # Показывает все данные     
stadium.display_data(show_city=False)  # Показывает данные без назание города                




