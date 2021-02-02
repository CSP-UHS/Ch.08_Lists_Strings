import random

class Player():
    def __init__(self):
        self.ac = 16
        self.hp = 10
        self.stats = ["Str", "Con", "Dex", "Wis", "Int", "Cha"]
        self.weapon = "Fists"
        self.shield = None
        self.inventory = []

def pseudopod():
    attack = random.randint(1, 21) + 3
    if attack >= Player.hp:
        damage = (random.randint(1, 7) + 1) + random.randint(1, 7) + random.randint(1, 7)
class Slime():
    def __init__(self):
        self.ac = 8
        self.hp = 22
        self.stats = [12, 6, 16, 1, 6, 2]
        self.attack = [pseudopod()]
