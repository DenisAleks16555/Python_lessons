autos = ('bmv', 'audi', 'ford', 'tesla')
print(autos)

user_choise, rename = input("Введите марку автомобиля и слово для замены ").split()
count = autos.count(user_choise)


def is_equal(x):
    if x== user_choise:
      return rename
    else:
       return x


if count:
    #autos = tuple(map(lambda x: rename if x== user_choise else x,autos))
    autos = tuple(map(is_equal, autos))
print(autos)