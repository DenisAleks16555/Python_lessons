
def hello():
    print('Hello World!')

# hello()

def new_abilliti(func):
    def wrapper():
        print("Функционал перед функцией")
        func()
        print("Функционал после функции")
    return wrapper

# new_abilliti(hello)
hello = new_abilliti(hello)
hello()

