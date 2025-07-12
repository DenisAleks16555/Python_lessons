class Book:
    def __init__(self, name, autor, year):
        self.name = name
        self.autor = autor
        self.year = year


    def __str__(self):
        return f"{self.name}\n{self.autor}\n{self.year}"
Buratino = Book('Буратино', 'Алексей Толстой', '1899')

 
print(Buratino)
    
 