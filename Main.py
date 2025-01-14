global enemyHP, yourweapons, yourmoney
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

    def attack(self, strength):
        global enemyHP
        if self.name in yourweapons:
            if strength/10 >= self.weight:
                enemyHP -= self.damage
                return True
            else:
                print(f"You are not strong enough to pick up the {self.name}")
            return False
        else:
            print("You don't have that weapon.")
            return False

    def buy(self):
        global yourmoney, yourweapons
        if yourmoney >= self.cost:
            yourmoney -= self.cost
            print(f"You buy a {self.name} for ${self.cost}")
            yourweapons.append(self.name)

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

    def attack(self, strength):
        if super().attack(strength):
            print(f"You slash with your {self.name}")



class Bow(Weapon):

    def __init__(self, name, range, material, damage, cost, weight):
        super().__init__(name, range, material, damage, cost, weight)

    def attack(self, strength):
        if super().attack(strength):
            print(f"You shoot with your {self.name}")


slasher = Sword("Slasher", 1, "steel", 20, 100, 7)
apollos_bow = Bow("Apollo's Bow", 200, "wood", 10, 200, 4)

apollos_bow.buy()
apollos_bow.attack(1000)