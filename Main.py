enemyHP = 1000
yourweapons = []
yourmoney = 10000

class Weapon:

    def __init__(self, name, range, material, damage, cost, weight):
        self.name = name
        self.range = range
        self.material = material
        self.damage = damage
        self.cost = cost
        self.weight = weight

    def attack(self):
        pass

    def buy(self):
        if yourmoney >= self.cost:
            yourmoney -= self.cost
            print(f"You buy a {self.name} for ${self.cost}")
            yourweapons.append(self)

    def examine(self):
        parameters = {
            "range" : self.range,
            "material" : self.material,
            "damage" : self.damage,
            "cost" : self.cost,
            "weight" : self.weight
        }
        print(f"These are the parameters of your weapon- {self.name}\n{parameters}")


class Sword(Weapon):

    def __init__(self, name, range, material, damage, cost, weight):
        super().__init__(name, range, material, damage, cost, weight)

    def attack(self):
        print(f"You slash with your {self.name}")
        enemy

slasher = Sword("Slasher", 5, "wood", 5, 100, 7)