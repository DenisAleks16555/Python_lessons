class Stack:
    def __init__(self, max_size):
        # max_size - максимальный размер стека
        self.max_size = max_size
        self.items = []  # сюда будем складывать строки

    def push(self, item):
        # Добавить строку в стек, если не полный
        if self.is_full():
            print("Стек полный! Нельзя добавить строку.")
        else:
            self.items.append(item)
            print(f'Строка "{item}" добавлена в стек.')

    def pop(self):
        # Убрать верхнюю строку и вернуть её
        if self.is_empty():
            print("Стек пуст! Нечего удалять.")
            return None
        else:
            item = self.items.pop()
            print(f'Строка "{item}" удалена из стека.')
            return item

    def count(self):
        # Сколько строк в стеке
        return len(self.items)

    def is_empty(self):
        # Проверка, пуст ли стек
        return len(self.items) == 0

    def is_full(self):
        # Проверка, полный ли стек
        return len(self.items) >= self.max_size

    def clear(self):
        # Очистить стек
        self.items = []
        print("Стек очищен.")

    def peek(self):
        # Посмотреть верхнюю строку, не удаляя
        if self.is_empty():
            print("Стек пуст! Нет верхней строки.")
            return None
        else:
            return self.items[-1]  # последний элемент списка

def main():
    size = int(input("Введите максимальный размер стека: "))
    stack = Stack(size)

    while True:
        print("\nВыберите действие:")
        print("1. Добавить строку в стек")
        print("2. Убрать верхнюю строку из стека")
        print("3. Узнать количество строк в стеке")
        print("4. Проверить, пуст ли стек")
        print("5. Проверить, полный ли стек")
        print("6. Очистить стек")
        print("7. Посмотреть верхнюю строку")
        print("8. Выйти")

        choice = input("Введите номер действия: ")

        if choice == "1":
            s = input("Введите строку для добавления: ")
            stack.push(s)

        elif choice == "2":
            stack.pop()

        elif choice == "3":
            print(f"В стеке сейчас {stack.count()} строк(и).")

        elif choice == "4":
            if stack.is_empty():
                print("Стек пуст.")
            else:
                print("Стек не пуст.")

        elif choice == "5":
            if stack.is_full():
                print("Стек полный.")
            else:
                print("Стек не полный.")

        elif choice == "6":
            stack.clear()

        elif choice == "7":
            top = stack.peek()
            if top is not None:
                print(f'Верхняя строка: "{top}"')

        elif choice == "8":
            print("Выход из программы.")
            break

        else:
            print("Неверный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()

