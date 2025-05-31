def str_upper(s):
    return s.upper()

def str_lower(s):
    return s.lower()

def str_title(s):
    return s.title()

def str_change(st, func):# Функция высшего порядка принимает строку и ссылку на   какую-нибудь функцию
    print(func(st))
str_change("Hello", str_upper)
str_change("Hello", str_lower)
str_change("Hello", str_title)