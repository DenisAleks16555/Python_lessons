class Airplane:
    def __init__(self, plane_type, max_passengers):
        self.plane_type = plane_type
        self.max_passengers = max_passengers
        self.current_passengers = 0  # начальное число пассажиров

    def __eq__(self, other):
        # Проверка, одинаковый ли тип самолётов
        return self.plane_type == other.plane_type

    def __gt__(self, other):
        # Сравниваем по максимальному количеству пассажиров
        return self.max_passengers > other.max_passengers
    
    def __lt__(self, other):
        # Сравниваем по максимальному количеству пассажиров
        return self.max_passengers < other.max_passengers
    
    def __ge__(self, other):
        # Сравниваем по максимальному количеству пассажиров
        return self.max_passengers >= other.max_passengers
    
    def __le__(self, other):
        # Сравниваем по максимальному количеству пассажиров
        return self.max_passengers <= other.max_passengers
    
    def __iadd__(self, value):
        # увеличиваем число пассажиров
        self.current_passengers += value
        # не допускаем превышения максимума
        if self.current_passengers > self.max_passengers:
            self.current_passengers = self.max_passengers
        return self  # Возвращаем объект после изменения

    def __isub__(self, value):
        # уменьшаем число пассажиров
        self.current_passengers -= value
        # не допускаем отрицательное число
        if self.current_passengers < 0:
            self.current_passengers = 0
        return self  # Возвращаем объект после изменения

    def __str__(self):
        return (f"Самолёт типа {self.plane_type}, максимум пассажиров: {self.max_passengers}, текущие пассажиры: {self.current_passengers}")


# Пример использования
airplane1 = Airplane("Боинг 737", 180)
airplane1 += 150  # Добавляем 150 пассажиров
print(airplane1)

airplane1 -= 50  # Уменьшаем на 50 пассажиров
print(airplane1)