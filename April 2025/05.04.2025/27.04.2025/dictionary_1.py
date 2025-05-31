bsk ={

}

pl = {
    "name": "Макс",
    "fname": "Максимов",
    "height": 198
}


def creat_player():
    name = input("Введите имя игрока: ")
    fname = input("Введите фамилию игрока: ")
    height = int(input("Введите рост игрока: "))
    return {"name": name, "fname": fname, "height": height}

def add_player(player: dict):
    id = tuple(player.values()) # Переводим в кортеж
    bsk[id] = player


def del_player(player: dict):
    id = tuple(player.values())
    del bsk[id] # - функция удаления 
    print(f"{player["name"]} {player["fname"]} Успешно удалён из списка")
    


def find_player(text: str):
    for player in bsk.values():
        if text in player.values():
            print(player)

def change_player(old_player: dict, new_player: dict):
    del_player(old_player) # Удаление игрока
    add_player(new_player) # Добавить игрока




# print(bsk)
# pl_1 = creat_player() # Создание игрока
# add_player(pl_1) # Добавление игрока
# print(bsk)
# add_player(creat_player())
# print(bsk)

# add_player(pl)
# print(bsk)
# del_player(pl) # Удаление игрока
# print(bsk)

add_player(pl)
print(bsk)
find_player("Макс") # Найти игрока
print(bsk)