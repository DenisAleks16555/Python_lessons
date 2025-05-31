lst = [10, 12, 13, "apple", 15, True, 34]
for elem in lst:
    print(elem)

    # for i in range(len(lst)):#  для каждого элемента в диапозоне
        # print(i)

for i in range(len(lst)):#  для каждого элемента в диапозоне от 0 до 6
        lst[i] = i + 10 # к каждому индексу прибавляем 10
        print(lst)