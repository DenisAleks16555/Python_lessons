
def is_simple_number(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

lst = [3, 65, 7, 10]
for i in lst:
    print(is_simple_number(i))