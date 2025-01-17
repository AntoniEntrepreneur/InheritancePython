"""
Author: Antoni Pieszczoch
Date: 7.01.2025
Course: Python I, Lab 13
Assignment: Programowanie obiektowe- dziedziczenie
Description:
    Gra, która prezentuje działanie dziedziczenia na przykładzie różnych bronii- łuku, miecza itd.
Version: 1.0
Notes:
"""



import random, time

global enemyHP, yourweapons, yourmoney, HP
enemyHP = 1000
yourweapons = []
yourmoney = 10000
space = 30

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
            enemyHP -= self.damage * 8
        if bodypart_hit == "eye":
            time.sleep(1)
            print("You hit your enemy in the eye")
            enemyHP -= self.damage * 50
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

class Rock(Weapon):

    def __init__(self, name = "rock", range = 10, material = "stone", cost = 0, damage = 10, weight = 3, accuracy = "low"):
        super().__init__(name = "rock", range = 10, material = "stone", cost = 0, damage = 10, weight = 3, accuracy = "low")

    def attack(self, strength):
        print(f"You throw a rock")
        super().attack(strength)


def check_enemyHP():
    global enemyHP
    print(f"Enemy's HP is at {enemyHP}")

def buy_a_weapon():
    still_buying = True
    while still_buying:
        weapon_to_buy = input("What weapon do you want to buy (Nothing / 1- Slasher / 2- Apollo's Bow / 3- Excalibur): ")
        if weapon_to_buy.lower() == "nothing":
            print("You don't buy anything")
            still_buying = False
        else:
            try:
                if int(weapon_to_buy) == 1:
                    slasher.buy()
                elif int(weapon_to_buy) == 2:
                    apollos_bow.buy()
                elif int(weapon_to_buy) == 3:
                    excalibur.buy()
                still_buying = False
            except ValueError:
                print(f"{weapon_to_buy} is not the right input. Choose 1/2/3")
                still_buying = True

def fight():
    print(f"You start a fight!")
    choosing_fighting_weapon = True
    while choosing_fighting_weapon:
        fighting_weapon = int(input("Choose your weapon (1- Slasher / 2- Apollo's Bow / 3- Excalibur / 4- Pick up a rock): "))
        choosing_fighting_weapon = False
        if fighting_weapon == 1:
            slasher.attack(1000)
        elif fighting_weapon == 2:
            apollos_bow.attack(1000)
        elif fighting_weapon == 3:
            excalibur.attack(1000)
        elif fighting_weapon == 4:
            rock.attack(1000)
        else:
            print("Input 1/2/3")
            choosing_fighting_weapon = True

def move(m, d):
    global space
    if d.lower() == "forward":
        space -= m
    elif d.lower() == "backward":
        space -= m

slasher = Sword("Slasher", 1, "steel", 20, 100, 7, "high")
apollos_bow = Bow("Apollo's Bow", 200, "wood", 10, 200, 4, "medium")
excalibur = Sword("Excalibur", 1.5, "mystical_material", 200, 9000, 10, "high")
rock = Rock()

def main_loop():
    running = True
    while running:
        if enemyHP <= 0:
            print("You have defeated your enemy!")
            running = False
        else:
            action = input("What do you want to do? (Buy a weapon / Check enemy's HP / Sell a weapon / Examine a weapon / Check money / Fight / Move):\n")

            # Buying a weapon
            if action.lower() == "buy a weapon":
                buy_a_weapon()

            # Checking enemy's HP
            elif action.lower() == "check enemy's hp":
                check_enemyHP()

            # Selling a weapon
            elif action.lower() == "sell a weapon":
                weapon_to_sell = input("What weapon do you want to sell?: ")
                if weapon_to_sell.lower() == "slasher":
                    if slasher.name in yourweapons:
                        slasher.sell()
                    else:
                        print(f"You don't have the Slasher")
                    if apollos_bow.name in yourweapons:
                        apollos_bow.sell()
                    else:
                        print(f"You don't have the Apollo's Bow")
                    if excalibur.name in yourweapons:
                        excalibur.sell()
                    else:
                        print(f"You don't have the Excalibur")

            # Examining a weapon
            elif action.lower() == "examine a weapon":
                weapon_to_examine = input("What weapon do you want to examine?: ")
                if weapon_to_examine.lower() == "slasher":
                    if slasher.name in yourweapons:
                        slasher.examine()
                    else:
                        print(f"You don't have the Slasher")
                if weapon_to_examine.lower() == "apollo's bow":
                    if apollos_bow.name in yourweapons:
                        apollos_bow.examine()
                    else:
                        print(f"You don't have the Apollo's Bow")
                if weapon_to_examine.lower() == "excalibur":
                    if excalibur.name in yourweapons:
                        excalibur.examine()
                    else:
                        print(f"You don't have the Excalibur")

            # Checking money
            elif action.lower() == "check money":
                print(f"You have ${yourmoney}")

            # Fighting
            elif action.lower() == "fight":
                fight()
            
            # Moving
            elif action.lower() == "move":
                print(f"The distance is {space}m")
                decision = True
                while decision:
                    decision = False
                    d = input("How do you want to move? (forward/backward): ")
                    m = int(input("How many meters do you want to move? "))
                    if d == "forward" and m > space:
                        print("You are closer than that")
                        decision = True
                move(m, d)
                print(f"Now the distance is {space}")

            # Incorrect input to action
            else:
                print("Incorrect input")

main_loop()