class MagicItem:
    def __init__(self, name, power_level):
        self.name = name
        self.power_level = power_level

    def __str__(self):
        return f"Магический предмет: {self.name}"

    def __repr__(self):
        return f"MagicItem('{self.name}', {self.power_level})"

    def __lt__(self, other):
        return self.power_level < other.power_level

    def __eq__(self, other):
        return (self.name == other.name) and (self.power_level == other.power_level)

 
# Пример
item1 = MagicItem("Fire Wand", 5)
item2 = MagicItem("Ice Wand", 7)
item3 = MagicItem("Fire Wand", 5)

print(item1 < item2)     # True, потому что 5 < 7
print(item1 == item3)    # True, потому что имя и уровень совпадают
print(str(item1))        # Магический предмет: Fire Wand
print(repr(item2))       # MagicItem('Ice Wand', 7)