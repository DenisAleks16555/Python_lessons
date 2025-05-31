def new_abilliti(func):
    def wrapper():
        print("Функционал перед функцией")
        func()
        print("Функционал после функции")
    return wrapper

# hello = new_abilliti(hello)
@ new_abilliti
def hello():
    print('Hello World!')

hello()

