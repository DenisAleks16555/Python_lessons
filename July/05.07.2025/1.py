class Zanachka:
    def __init__(self):
        self.__count = 0
    def view_cach(self): # посмотреть сколько у нас денег в капилке
        return self.__count # Чему равен на текущий момент кеш
    def add_cach(self, add_to_cach): # дорбавить деньги
        if add_to_cach >=0: #не можем прописать отрицательную сумму
            self.__count += add_to_cach

    def withdraw_cach(self, withdraw_to_cach ): # изымаем какую-то сумму
        if self.__count >= withdraw_to_cach:
            self.__count -= withdraw_to_cach
        else:
            print("В заначке недостаточно средств")

    
aleksandr = Zanachka()

print(aleksandr.view_cach())

aleksandr.add_cach(50_000)

print(aleksandr.view_cach())

aleksandr.withdraw_cach(1000)

print(aleksandr.view_cach())

aleksandr.withdraw_cach(60_000)

print(aleksandr.view_cach())

aleksandr.add_cach(-50_000)
print(aleksandr.view_cach())

aleksandr.__count = 1_000_000
print(aleksandr.view_cach())