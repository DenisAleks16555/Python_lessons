employers = [
           ["Иван", "Иванов", 1000, 20],
           ["Сергей", "Сергеев", 800, 35],
           ["Светлана", "Иванова", 1500, 15],
           ["Анатолий", "Червяк", 2000, 1],
           ["Арнольд ", "Шварцнегер", 3000, 0],
           ["Сильвестр", "Сталоне", 300, 60],
                                   
                             
            ]

employers = list(map(lambda x: x + [x[2] * x[3]], employers))
for i in employers:
    print(i)

employers.sort(key=lambda x: x[4], reverse=True)

print('='*35)
for i in employers:
    print(i)



employers.sort(key=lambda x: x[1][1]) # Степень вложенности

print('='*35)
for i in employers:
    print(i)

# employers = list(map(lambda x: [x[1]] + [x[0]] + x[2:], employers))
employers = list(map(lambda x: x[1::-1] + x[2:], employers))
print('='*35)
for i in employers:
    print(i)

print(employers[2][1][2]) # Выводим Арнольд, третью  букву в Арнольд



                                   
                                  

