class Warrior():

    def __init__(self, name, power, endurance, hair_color):
        self.name = name
        self.power = power
        self.endurance = endurance
        self.hair_color = hair_color

    def sleep(self):
        print(f"{self.name} лег спать")
        self.endurance += 2

    def eat(self):
        print(f"{self.name} сел кушать")
        self.power += 1

    def hit(self):
        print(f"{self.name} бъет кого-то")
        self.endurance -= 1

    def walk(self):
        print(f"{self.name} гуляет")
        self.endurance -= 1

    def info(self):
        print(f"Имя: {self.name}")
        print(f"Сила: {self.power}")
        print(f"Выносливость: {self.endurance}")
        print(f"Цвет волос: {self.hair_color}")

war1 = Warrior("Вася", 76, 54, "черный")
war2 = Warrior("Петя", 45, 32, "белый")

war1.info()
