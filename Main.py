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
        print(f"You buy a {self.name} for ${self.cost}")

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
