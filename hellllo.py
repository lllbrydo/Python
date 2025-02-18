from random import randint


class kosmonavt:
    def __init__(self, name):
        self.name = name
        self.fuel = 100
        self.health = 100
        self.oxygen = 100
        self.alive = True

    def explore(self):
        print("Ізучати нову планету")
        self.fuel -= 10
        self.oxygen -= 15
        if randint(1, 5) == 1:
            print("Знайдено артефакт")
            self.health += 10
        else:
            print("Пусто")

    def remont(self):
        print("Ремонт корабля")
        self.fuel += 20
        self.health += 15

    def relax(self):
        print("Відпочинок")
        self.oxygen += 20
        if self.oxygen > 100:
            self.oxygen = 100

    def is_alive(self):
        if self.fuel <= 0:
            print("Немає палива")
            self.alive = False
        elif self.health <= 0:
            print("Астронавт загинув")
            self.alive = False
        elif self.oxygen <= 0:
            print("Немає кисню")
            self.alive = False
        elif randint(1, 100) > 95:
            print("Нова галактика відкрита")
            self.alive = False

    def status(self):
        print(f"Паливо {self.fuel}")
        print(f"Здоровя {self.health}")
        print(f"Кисень {self.oxygen}\n")

    def live(self, day):
        print(f"День {day} Астронавт {self.name}")
        action = randint(1, 3)
        if action == 1:
            self.explore()
        elif action == 2:
            self.remont()
        elif action == 3:
            self.relax()
        self.status()
        self.is_alive()

nazar = kosmonavt("назар")

for day in range(1, 51):
    if not nazar.alive:
        break
    nazar.live(day)