# 3 типа ошибок:
# 1 ошибка
try:
    dct = {
        [1,2,3]: "start",
    }
# 2 ошибка
    print(int("a"))
    print(1/0)
# 3 ошибка
except Exception as e:
    print(type(e).__name__) # Выведется название ошибки
    print(e) # Выведется эта ошибка