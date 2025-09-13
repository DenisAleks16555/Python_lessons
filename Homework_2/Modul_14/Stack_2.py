class StringStack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.stack = []

    def push(self, string):
        if self.is_full():
            print("Стек полон, не можем добавить строку.")
        else:
            self.stack.append(string)
            print(f"Добавлено: {string}")

    def pop(self):
        if self.is_empty():
            print("Стек пуст, нечего удалять.")
        else:
            removed = self.stack.pop()
            print(f"Удалено: {removed}")

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.max_size

    def clear(self):
        self.stack = []
        print("Стек очищен.")

    def peek(self):
        if self.is_empty():
            print("Стек пуст.")
        else:
            print(f"Верхняя строка: {self.stack[-1]}")

# Меню для взаимодействия
def menu():
    max_size = int(input("Введите размер стека: "))
    stack = StringStack(max_size)

    while True:
        print("\nМеню:")
        print("1. Поместить строку в стек")
        print("2. Вытолкнуть строку из стека")
        print("3. Посчитать количество строк")
        print("4. Проверить, пуст ли стек")
        print("5. Проверить, полный ли стек")
        print("6. Очистить стек")
        print("7. Получить верхнюю строку без удаления")
        print("0. Выйти")
        choice = input("Выберите операцию: ")

        if choice == '1':
            s = input("Введите строку: ")
            stack.push(s)
        elif choice == '2':
            stack.pop()
        elif choice == '3':
            print(f"Количество строк: {stack.size()}")
        elif choice == '4':
            print("Стек пуст" if stack.is_empty() else "Стек не пуст")
        elif choice == '5':
            print("Стек полный" if stack.is_full() else "Стек не полный")
        elif choice == '6':
             stack.clear()
        elif choice == '7':
            stack.peek()
        elif choice == '0':
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите операцию из меню.")

# Запуск меню
if __name__ == "__main__":
    menu()
# Пример использования класса StringStack

    # Создание стека с максимальным размером 3
    stack = StringStack(3)

    # Добавление строк в стек
    stack.push("Первая строка")  # Ожидаем: Добавлено: Первая строка
    stack.push("Вторая строка")   # Ожидаем: Добавлено: Вторая строка
    stack.push("Третья строка")    # Ожидаем: Добавлено: Третья строка
    stack.push("Четвертая строка")  # Ожидаем: Стек полон, не можем добавить строку.


            