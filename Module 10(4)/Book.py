class Book:
    def __init__(self, title, year, publisher, genre, author, price):
        """Инициализация атрибутов книги."""
        self.title = title          # Название книги
        self.year = year            # Год выпуска
        self.publisher = publisher  # Издатель
        self.genre = genre          # Жанр
        self.author = author        # Автор
        self.price = price          # Цена

    def input_data(self):
        """Метод для ввода данных о книге."""
        self.title = input("Введите название книги: ")
        self.year = int(input("Введите год выпуска: "))
        self.publisher = input("Введите издателя: ")
        self.genre = input("Введите жанр: ")
        self.author = input("Введите автора: ")
        self.price = float(input("Введите цену: "))

    def display_data(self, show_price=True):
        """Метод для вывода данных о книге с возможностью скрыть цену."""
        print(f"Название: {self.title}")
        print(f"Год выпуска: {self.year}")
        print(f"Издатель: {self.publisher}")
        print(f"Жанр: {self.genre}")
        print(f"Автор: {self.author}")
        if show_price:
            print(f"Цена: {self.price}")
    
# Создаем объект книги через конструктор
book1 = Book("1984", 1949, "Secker & Warburg", "Dystopian", "George Orwell", 15.99)

# Выводим данные книги
book1.display_data()            # Показывает все данные

book1.display_data(show_price=False)  # Показывает данные без цены