w = 15
h = 4

# for i in range(h):
    # for j in range(w):
        # print("*", end='')
    # print()
#Генирируем строки из 15 звёздочек
for i in range(h):
    print( *["*" for j in range(w)]) #в одной строчке вложено несколько операций,что написаны вверху
  
      
    