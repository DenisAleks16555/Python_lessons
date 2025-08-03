
misicians = {
       'Linkin Park' : ["Reanimation", "Hybrid Theory"],
       "Rammstein" : ["Mutter", "Zeit"],
       "Мияги" : ["Ямакаси", "Бастер Китон"]
}

def show_menu():    
    print("Выберите операцию:")
    print("1 - Выбрать группу:")
    print("2 - Добавить группу:")
    print("3 - Удалить группу:")
    print("4 - Выход:")

    while True:
        show_menu()
        choise = int(input())
        if choise == 1:
            group = input("Введите название группы: ")
            if misicians.get("group_for_add", None) is not None:
                print(misicians.get("group_for_add", None))
            else:
                print(f"Группы {group_for_add} нет в каталоге!")

        elif choise == 2:
            group_for_add = input("Введите название группы для добавления")
            if misicians.get("group_for_add", None) is not None:
                print(f"Группа {group_for_add} уже есть в каталоге")
            else:
                misicians[group_for_add] = []
                print(f"Группа {group_for_add} добавлена в каталог!")

        elif choise == 3:
            group_for_del = input("Введите название группы для удаления: ")
            try:
                misicians.pop(group_for_del)
                print(f"Группа {group_for_del} успешна удалена!")
            except:
                print("Такой группы нет в каталоге")
                
        elif choise == 4:
            print("Выходим из программы")
            break

        else:
            print("Введена некорректная команда")

        input("Нажмите 'Enter' для продолжения")
