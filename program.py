import random

from actors import Creature, Wizard, SmallCreature, Dragon


def draw_header():
    print('---------------------------')
    print('     Wizard Battle App')
    print('---------------------------')
    print()


def game_loop():
    player = Wizard('Wizardy Boy', 50)
    creatures = [SmallCreature('Rat', 1),
                 Creature('Golem', 20),
                 Dragon('Dragon (His name is Freddy)', 70, 20, True),
                 Wizard('Evil Wizardy Boy', 200)]
    current_enemy = random.choice(creatures)

    while True:
        print('You encounter a terrifying {}!'.format(current_enemy.name))
        action = input('Do you want to [A]ttack, [L]ook around or [R]un away?')
        action = action.lower()
        if action == 'a':
            result = player.attack(current_enemy)
            if result:
                print('You win buddy!')
                current_enemy = random.choice(creatures)
            else:
                print('You dead.')
                break

        elif action == 'l':
            print('You look around and see:')
            for c in creatures:
                print(c.name)

        elif action == 'r':
            print('You run away from the {}!'.format(current_enemy))
            current_enemy = random.choice(creatures)

        else:
            print('Bye forever!')
            break


def main():
    draw_header()
    game_loop()


if __name__ == '__main__':
    main()
