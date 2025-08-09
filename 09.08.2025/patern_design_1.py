# Задание по Патерному проектированию
class Publisher:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, obj): # Подписаться
        self.subscribers.append(obj)

    def unsubscribe(self, obj): # Отписаться
        self.subscribers.remove(obj)

    def notify(self, data: dict): # Уведомление
        for sub in self.subscribers: # sub - Для каждого подписчика
            sub.update(data)

    
    # Реализуем класс подписчика, который что-то будет делать с этим уведомлением
class Subscriber:
    def __init__(self, name):
        self.name = name
# метод update 
    def update(self, data: dict):
        print(f"Подписчик {self.name} получил уведомление: {data["type"]} id {data["id"]}")


order = Publisher()

kitchen = Subscriber("кухня")
count = Subscriber("бухгалтерия")
# Подписываемся на наши уведомления
order.subscribe(kitchen)
order.subscribe(count)

order.notify({"type": "заказ", "id": "001", "phone": "8-800-555-35-35"}) # Какая-то информация о нашем заказе

