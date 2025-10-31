class Stack:
    def __init__(self):
        # Теперь стек не имеет максимального размера
        self.items = []  # список для хранения строк

    def push(self, item):
        # Просто кладём строку в стек
        self.items.append(item)
        print(f'Строка "{item}" добавлена в стек.')

    def pop(self):
        # Убираем верхнюю строку, если стек не пустой
        if self.is_empty():
            print("Стек пуст! Нечего удалять.")
            return None
        else:
            item = self.items.pop()
            print(f'Строка "{item}" удалена из стека.')
            return item

    def count(self):
        # Возвращаем количество строк в стеке
        return len(self.items)

    def is_empty(self):
        # Проверяем, пуст ли стек
        return len(self.items) == 0

    def clear(self):
        # Очищаем стек
        self.items = []
        print("Стек очищен.")

    def peek(self):
        # Смотрим верхнюю строку, не удаляя
        if self.is_empty():
            print("Стек пуст! Нет верхней строки.")
            return None
        else:
            return self.items[-1]

def main():
    stack = Stack()  # создаём стек без ограничения размера

    while True:
        print("\nВыберите действие:")
        print("1. Добавить строку в стек")
        print("2. Убрать верхнюю строку из стека")
        print("3. Узнать количество строк в стеке")
        print("4. Проверить, пуст ли стек")
        print("5. Очистить стек")
        print("6. Посмотреть верхнюю строку")
        print("7. Выйти")

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
            stack.clear()

        elif choice == "6":
            top = stack.peek()
            if top is not None:
                print(f'Верхняя строка: "{top}"')

        elif choice == "7":
            print("Выход из программы.")
            break

        else:
            print("Неверный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()

