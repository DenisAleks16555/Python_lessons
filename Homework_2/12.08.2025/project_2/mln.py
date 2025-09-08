import json


with open(r"c:\Users\0\OneDrive\Рабочий стол\MyPythonProjects\Python_lessons\12.08.2025\project_2\data.json", 'r', encoding='utf-8') as file:
    data = json.load(file)
# with open('data.json', 'r', encoding='utf-8') as file:
#     data = json.load(file)
# Выводим информацию
print(f'product: {data["product"]}')
print(f'price: {data["price"]}')
print(f'In stock: {data["in_stock"]}')