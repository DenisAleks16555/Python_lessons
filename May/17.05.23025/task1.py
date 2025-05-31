# Задачи:
posts = [
    {"likes" : 5, "comments": 3, "reposts":1},
    {"comments": 4, "reposts": 2},
    {"likes": 2},
    {"likes" : 3, "comments": 1, "reposts":1},
    {"likes" : 10, "comments": 50, "reposts":5},

]

total_likes = 0
for i in posts:
    # первый вариант
    total_likes += i.get("likes", -2) # Метод словарей get
    # Второй вариант
    #   try:
    #       total_likes += i["likes"] # Сохраняем в переменную и считаем сколько у нас like
    #   except:
    #       total_likes -= 2

print(total_likes)