class Money:
    """
    Класс для представления суммы денег с целой и дробной частью.
    """

    def __init__(self, whole_part=0, fractional_part=0):
        """
        Конструктор класса Money.
        :param whole_part: Целая часть суммы (доллары, евро, гривны и т.д.).
        :param fractional_part: Дробная часть суммы (центы, евроценты, копейки и т.д.).
        """
        print(f"Создаем объект Money с целой частью: {whole_part}, дробной частью: {fractional_part}")
        self.whole_part = whole_part
        self.fractional_part = fractional_part

    def display_money(self):
        """
        Выводит сумму денег на экран в формате: ЦелаяЧасть.ДробнаяЧасть (с двумя знаками для дробной части).
        """
        print(f"{self.whole_part}.{self.fractional_part:02d}")

    def set_whole_part(self, value):
        """
        Устанавливает новую целую часть суммы.
        :param value: Новое значение для целой части. Должно быть целым числом.
        """
        if isinstance(value, int):
            self.whole_part = value
            print(f"Целая часть установлена на: {self.whole_part}")
        else:
            print(f"Ошибка: Невозможно установить целую часть. Значение '{value}' не является целым числом.")

    def set_fractional_part(self, value):
        """
        Устанавливает новую дробную часть суммы.
        :param value: Новое значение для дробной части. Должно быть целым числом от 0 до 99.
        """
        if isinstance(value, int) and 0 <= value <= 99:
            self.fractional_part = value
            print(f"Дробная часть установлена на: {self.fractional_part}")
        else:
            print(f"Ошибка: Невозможно установить дробную часть. Значение '{value}' должно быть целым числом от 0 до 99.")

# --- Пример использования ---

print("--- Создание и вывод объектов ---")

# Создаем объект с указанными значениями
dollar_amount = Money(15, 30)  # 15 долларов, 30 центов
dollar_amount.display_money() # Вывод: 15.30

# Создаем объект, указывая только дробную часть (целая часть будет 0)
euro_amount = Money(fractional_part=75) # 0 евро, 75 евроцентов
euro_amount.display_money() # Вывод: 0.75

# Создаем объект, используя все значения по умолчанию (0.00)
ruble_amount = Money() # 0 рублей, 0 копеек
ruble_amount.display_money() # Вывод: 0.00

print("\n--- Изменение значений объектов ---")

# Изменяем значения у объекта dollar_amount
dollar_amount.set_whole_part(20)
dollar_amount.set_fractional_part(5)
dollar_amount.display_money() # Вывод: 20.05

# Пытаемся установить некорректные значения
euro_amount.set_whole_part("сто") # Ошибка, целая часть не установлена
euro_amount.set_fractional_part(150) # Ошибка, дробная часть не установлена
euro_amount.display_money() # Вывод останется прежним: 0.75

ruble_amount.set_whole_part(100)
ruble_amount.set_fractional_part(99)
ruble_amount.display_money() # Вывод: 100.99
