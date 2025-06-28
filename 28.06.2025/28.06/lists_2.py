dct = {
    "a": 1,
    "b": 2,
    "c": 3
}
dct["d"] = 4

keys = list(dct.keys())
volues = list(dct.values())
#название словаря точка
print(f"Список ключей:{keys}")
print(f"Список значений:{volues}")

# добавить ключ значение d: 4
new_dct = {value: key for key, value in dct.items()}
print(f"Перевёрнутый список {new_dct} ")

