def main():
    # Получаем список чисел
    numbers = input("Введите числа через пробел: ")
    numbers_list = [int(num) for num in numbers.split()]

    while True:
        print("\nВыберите действие:")
        print("1. Добавить число")
        print("2. Удалить число")
        print("3. Показать список")
        print("4. Проверить число")
        print("5. Заменить число")
        print("6. Выйти")

        choice = input("Введите номер действия: ")

        if choice == "1":
            num = int(input("Введите число для добавления: "))
            if num in numbers_list:
                print("Число уже есть в списке!")
            else:
                numbers_list.append(num)
                print("Число добавлено.")

        elif choice == "2":
            num = int(input("Введите число для удаления: "))
            if num in numbers_list:
                numbers_list = [x for x in numbers_list if x != num]
                print("Число удалено.")
            else:
                print("Число не найдено.")

        elif choice == "3":
            order = input("Показать с начала или с конца? (введите 'начало' или 'конец'): ")
            if order == "начало":
                print("Список:", numbers_list)
            elif order == "конец":
                print("Список:", numbers_list[::-1])
            else:
                print("Неверный ввод.")

        elif choice == "4":
            num = int(input("Введите число для проверки: "))
            if num in numbers_list:
                print("Число есть в списке.")
            else:
                print("Числа нет в списке.")

        elif choice == "5":
            old_num = int(input("Введите число, которое хотите заменить: "))
            if old_num not in numbers_list:
                print("Такого числа нет в списке.")
                continue
            new_num = int(input("Введите новое число: "))
            how = input("Заменить только первое вхождение или все? (введите 'первое' или 'все'): ")
            if how == "первое":
                index = numbers_list.index(old_num)
                numbers_list[index] = new_num
                print("Число заменено.")
            elif how == "все":
                numbers_list = [new_num if x == old_num else x for x in numbers_list]
                print("Все вхождения заменены.")
            else:
                print("Неверный ввод.")

        elif choice == "6":
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()

