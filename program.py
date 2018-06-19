from actors import Creature, Wizard, SmallCreature, Dragon


def draw_header():
    print('---------------------------')
    print('     Wizard Battle App')
    print('---------------------------')
    print()


def game_loop():
    while True:
        action = input('Do you want to [A]ttack, [L]ook around or [R]un away?').lower()
        if action is 'a':
            pass
        elif action is 'l':
            pass
        elif action is 'r':
            pass
        else:
            print('Bye forever!')
            break


def main():
    draw_header()


if __name__ == '__main__':
    main()
