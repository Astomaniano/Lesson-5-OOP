# Определите класс 'Account', имитирующий банковский счет. Класс должен иметь атрибуты для хранения
# идентификатора владельца, баланс счета и методы для депозита и снятия денег со счета, если их достаточно.

class Account():
    def __init__(self, id, balance=0):
        self.id = id
        self.balance = balance

    def deposit(self, money):
        if money > 0:
            self.balance += money
            print(f'Вы успешно пополнили баланс, сумма на счете {self.balance} ')

    def widthdraw(self, money):
        if money > self.balance:
            print('Недостаточно средств на счете')
        elif money <= self.balance:
            self.balance -= money
            print(f'Вы успешно сняли {money} с баланса, сумма на счете {self.balance}')

    def all_balance(self):
        print(f'Ваш баланс {self.balance} рублей')

man = Account(12994619, 1000)
man.all_balance()
man.widthdraw(488)
man.widthdraw(2000)
man.deposit(29304)