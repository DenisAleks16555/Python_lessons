class Device:
    def __init__(self, name, manufacturer):
        self.name = name
        self.manufacturer = manufacturer

    def get_info(self):
        return f"Устройство: {self.name}, Производитель: {self.manufacturer}"

    def turn_on(self):
        return f"{self.name} включено."

    def turn_off(self):
        return f"{self.name} выключено."


class CoffeeMachine(Device):
    def __init__(self, name, manufacturer, coffee_type):
        super().__init__(name, manufacturer)
        self.coffee_type = coffee_type

    def brew_coffee(self):
        return f"Готовлю {self.coffee_type} кофе."

    def set_coffee_type(self, coffee_type):
        self.coffee_type = coffee_type
        return f"Тип кофе установлен на {self.coffee_type}."


class Blender(Device):
    def __init__(self, name, manufacturer, power):
        super().__init__(name, manufacturer)
        self.power = power

    def blend(self):
        return f"{self.name} смешивает ингредиенты с мощностью {self.power} Вт."
    
    def set_power(self, power):
        self.power = power
        return f"Мощность {self.name} установлена на {self.power} Вт."

class MeatGrinder(Device):
    def __init__(self, name, manufacturer, power):
        super().__init__(name, manufacturer)
        self.power = power  # мощность мясорубки в ваттах

    def grind_meat(self):
        return f"{self.name} перемалывает мясо с мощностью {self.power} Вт."


# Создаем объекты устройств
coffee_machine = CoffeeMachine("Кофемашина1", "Philips", "эспрессо")
blender = Blender("Блендер1", "Bosch", 600)
meat_grinder = MeatGrinder("Мясорубка1", "Redmond", 800)

# Используем методы
print(coffee_machine.get_info())
print(coffee_machine.brew_coffee())

print(blender.get_info())
print(blender.blend())

print(meat_grinder.get_info())
print(meat_grinder.grind_meat())