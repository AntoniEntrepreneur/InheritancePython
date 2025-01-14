import random, time

global enemyHP, yourweapons, yourmoney
enemyHP = 1000
yourweapons = []
yourmoney = 10000

class Weapon:

    def __init__(self, name, range, material, damage, cost, weight, accuracy):
        self.name = name
        self.range = range
        self.material = material
        self.damage = damage
        self.cost = cost
        self.weight = weight
        self.accuracy = accuracy

    def check_weapon(self, strength):
        if self.name in yourweapons:
            if strength / 10 >= self.weight:
                return True
            else:
                print(f"You are not strong enough to pick up the {self.name}")
                return False
        else:
            print("You don't have that weapon.")
            return False

    def attack(self, strength):
        global enemyHP
        bodyparts = ["head", "eye", "stomach", "leg", "armor", "missed"]
        if self.accuracy == "low":
            weights = [5, 0.1, 10, 20, 30, 34.9]
        elif self.accuracy == "medium":
            weights = [30, 0.5, 40, 5, 20, 4.5]
        elif self.accuracy == "high":
            weights = [40, 2, 30, 7, 20, 1]
        bodypart_hit = random.choices(bodyparts, weights = weights, k = 1)[0]
        if bodypart_hit == "head":
            time.sleep(1)
            print("You hit your enemy in the head")
            enemyHP -= self.damage * 10
        if bodypart_hit == "eye":
            time.sleep(1)
            print("You hit your enemy in the eye")
            enemyHP -= self.damage * 100
        if bodypart_hit == "stomach":
            time.sleep(1)
            print("You hit your enemy in the stomach")
            enemyHP -= self.damage * 2
        if bodypart_hit == "leg":
            time.sleep(1)
            print("You hit your enemy in the leg")
            enemyHP -= self.damage * 0.5
        if bodypart_hit == "armor":
            time.sleep(1)
            print("You hit your enemy in the armor")
            enemyHP -= self.damage * 0.1
        if bodypart_hit == "missed":
            time.sleep(1)
            print("You've missed")

    def buy(self):
        global yourmoney, yourweapons
        if yourmoney >= self.cost:
            yourmoney -= self.cost
            print(f"You buy the {self.name} for ${self.cost}")
            yourweapons.append(self.name)
        else:
            print(f"You don't have enough money to buy {self.name}")

    def sell(self):
        global yourmoney, yourweapons
        yourmoney += self.cost
        print(f"You sell the {self.name} for ${self.cost}")
        yourweapons.remove(self.name)


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

    def __init__(self, name, range, material, damage, cost, weight, accuracy):
        super().__init__(name, range, material, damage, cost, weight, accuracy)

    def attack(self, strength):
        if super().check_weapon(strength):
            print(f"You slash with your {self.name}")
            super().attack(strength)


class Bow(Weapon):

    def __init__(self, name, range, material, damage, cost, weight, accuracy):
        super().__init__(name, range, material, damage, cost, weight, accuracy)

    def attack(self, strength):
        if super().check_weapon(strength):
            print(f"You shoot with your {self.name}")
            super().attack(strength)


def check_enemyHP():
    print(f"Enemy's HP is at {enemyHP}")




slasher = Sword("Slasher", 1, "steel", 20, 100, 7, "medium")
apollos_bow = Bow("Apollo's Bow", 200, "wood", 10, 200, 4, "low")
excalibur = Sword("Excalibur", 1.5, "mystical_material", 200, 9000, 10, "high")

running = True
while running:
    if enemyHP <= 0:
        print("You have defeated your enemy!")
        running = False
    else:
        weapon_to_buy = str(input("What weapon do you want to buy"))
        weapon_to_buy.lower().buy()