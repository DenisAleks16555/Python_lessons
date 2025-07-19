# Класс Gun(пистолет) 
# Характеристика count(количество выстрелов. В начале count = 0)
# метод shoot(выстрел) при вызове этого метода пишет "Пиф" + 1
# метод 2 shoots_count возвращает нам количество выстрелов
class Pif:
    def __init__(self):
        self.count = 0

    def shoot(self):
        print("Пиф")
        self.count +=1

    def shoot_count(self):
        return self.count
    
glok = Pif() 
glok.shoot()
        
print(glok.shoot_count())


