class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_items(self, item, price):
        self.items[item] = price
        print (f'{item} по цене {price} добавлено в магазин {self.name}')

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]
            print (f'{item} удалено из магазина {self.name}')
        else:
            return None

    def get_price(self, item):
        if item in self.items:
            return f'Цена {item} в магазине {self.name} - {self.items[item]}'
        else:
            return None

    def update_price(self, item, new_price):
        if item in self.items:
            self.items[item] = new_price
            print (f'Цена {item} в магазине {self.name} обновлена')
        else:
            return None

    def all_items(self):
        print(f'Ассортимент магазина {self.name}:')
        for i in self.items:
            print(i, ':', self.items[i])

Пятерочка = Store('Пятерочка', 'ул. Ленина, 5')
Магнит = Store('Магнит', 'ул. Пушкинская, 10')
Перекресток = Store('Перекресток', 'ул. Карла Маркса, 2')

Пятерочка.add_items('Хлеб', 10)
Пятерочка.add_items('Молоко', 15)

Магнит.add_items('Молоко', 20)
Магнит.add_items('Сыр', 30)

Перекресток.add_items('Хлеб', 5)
Перекресток.add_items('Молоко', 15)

Пятерочка.get_price('Хлеб')

Пятерочка.update_price('Хлеб', 20)
Пятерочка.get_price('Хлеб')

Магнит.remove_item('Банан')
Магнит.remove_item('Молоко')

Пятерочка.all_items()