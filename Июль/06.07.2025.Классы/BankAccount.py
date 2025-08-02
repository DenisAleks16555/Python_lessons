class BankAccount:
    def __init__(self):
        self._balance = 0  # начальный баланс

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            print("Сумма пополнения должна быть положительной")

    def withdraw(self, amount):
        if amount > self._balance:
            print("Недостаточно средств")
        elif amount <= 0:
            print("Сумма снятия должна быть положительной")
        else:
            self._balance -= amount


account = BankAccount()     # создаём объект счёта
account.deposit(100)        # пополняем на 100
print(account.balance)      # выводим баланс — 100

account.withdraw(30)        # снимаем 30
print(account.balance)      # теперь 70

account.withdraw(100)       # пытаемся снять 100 — больше, чем есть
# Выведет: Недостаточно средств

print(account.balance)      # баланс остался 70