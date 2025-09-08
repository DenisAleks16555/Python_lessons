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

    def display_data(self):
        """Метод для вывода данных о книге."""
        print(f"Название: {self.title}")
        print(f"Год выпуска: {self.year}")
        print(f"Издатель: {self.publisher}")
        print(f"Жанр: {self.genre}")
        print(f"Автор: {self.author}")
        print(f"Цена: {self.price}")

    def get_title(self):
        """Метод для получения названия книги."""
        return self.title

    def get_author(self):
        """Метод для получения автора книги."""
        return self.author

# Пример использования класса Book
book1 = Book("", 0, "", "", "", 0.0)  # Создаем объект книги с пустыми полями
book1.input_data()                    # Заполняем данные книги с помощью метода
book1.display_data()                  # Выводим данные книги

book = Book("Манускрипт MS 408", 2007,"Гелеос","Реальный документ","Тьерре Можене",850.0)
book.input_data()