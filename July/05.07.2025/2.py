# Создать класс дом
# Две характеристики 1 колличество комнат 2 - цвет дома
# Действия
# 1 - поркрасить дом в новый цвет
# 2 - добавить комнату

class house:
    def __init__(self):
        self.rooms = 2
        self.color = "White"

    def count_room(self): 
        self.rooms +=1
        return self.rooms
        

   
    def change_color(self, new_color):
         self.color = new_color 

new_home = house()
new_home.count_room()
new_home.change_color("black")
print(new_home.rooms)
print(new_home.color)