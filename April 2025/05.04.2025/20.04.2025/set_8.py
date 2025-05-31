# Генерация мноржества

files_list = ["photo.png",
               "photo1.png", 
               "Photo.png", 
               "photo.jpeg",
               "photo.txt", 
               "new_year.rar",
               "2025.docx",
               "Tree.PNG",
               "github.git",
               ".env",
               "bebepng",
               "tree.Png"
               ]
# Вывести файлы с расширением Png
st = {i.lower() for i in files_list if ".png" in i.lower()} # Генератор множества

for i in st:
    print(i)
