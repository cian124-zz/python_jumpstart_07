import random


class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return "Creature: {} of level {}".format(self.name, self.level)

    def defensive_roll(self):
        roll = random.randint(1, 12)
        attack = self.level * roll
        return attack


class Wizard(Creature):
    def __init__(self, name, level):
        super().__init__(name, level)

    def attack(self, enemy):
        w_roll = self.defensive_roll()
        e_roll = enemy.defensive_roll()
        print('You roll {}'.format(w_roll))
        print('The enemy {} rolls a {}'.format(enemy.name, e_roll))
        if w_roll >= e_roll:
            return True
        else:
            return False


class SmallCreature(Creature):
    def __init__(self, name, level):
        super().__init__(name, level)


class Dragon(Creature):
    def __init__(self, name, level, scaliness, breaths_fire):
        super().__init__(name, level)
        self.scaliness = scaliness
        self.breaths_fire = breaths_fire

    def defensive_roll(self):
        roll = super().defensive_roll()
        fire_modifier = 5 if True else 1
        roll = roll * (self.scaliness / 10) * fire_modifier
        return roll
