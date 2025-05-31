import random as r      # (Модуль рандом)

# for i in range(5):
# # Генератор псевдослучайных чисел
#     print(r.random()) # от 0 до 1 не включая 1

# for i in range(5):
#     print(r.randrange(2,100, 2)) 

# for i in range(5):
#     print(r.randint(90,100)) # Включает диапозон от левого края до правого включительно -  90, 100


lst = [i for i in range(10)] # создать последовательность от 0 до 10 не включая 10
print(r.choice(lst))

print(r.sample(lst, 4))
