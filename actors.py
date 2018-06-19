import random


class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level


class Wizard(Creature):
    def __init__(self):
        super.__init__()

    def attack(self):
        pass


class SmallCreature(Creature):
    pass


class Dragon(Creature):
    def __init__(self, scaliness, breaths_fire):
        super.__init__()
        self.scaliness = scaliness
        self.breaths_fire = breaths_fire
    pass


def defensive_roll(level):
    roll = random.randrange(1, 12)
    attack = level * roll
    return attack
