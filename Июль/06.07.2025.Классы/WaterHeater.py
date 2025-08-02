class WaterHeater:
    def __init__(self):
        self._temperature = 20  # начальная температура

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if 0 <= value <= 100:
            self._temperature = value
        else:
            print("Недопустимая температура!")

    def heat_up(self, delta):
        new_temp = self._temperature + delta
        self.temperature = new_temp


heater = WaterHeater()          # создаём объект
print(heater.temperature)       # выводим текущую температуру: 20

heater.heat_up(10)              # нагреваем на 10 градусов
print(heater.temperature)       # теперь температура 30

heater.temperature = 150        # пытаемся задать 150 — слишком много!
# Выведет: Недопустимая температура!

print(heater.temperature)       # температура осталась 30