import sys, random, time

try:
    import bext
except ImportError:
    print("This program requires bext module.")
    sys.exit()

WIDTH, HEIGHT = bext.size()
WIDTH -= 1

NUMBER_OF_LOGOS = 1
PAUSE_AMOUNT = 0.15

COLORS = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

UP_RIGHT = 'ur'
UP_LEFT = 'ul'
DOWN_RIGHT = 'dr'
DOWN_LEFT = 'dl'

DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)

COLOR = 'color'

X = 'x'
Y = 'y'
DIR = 'direction'

WORD = 'WORD'

def main():
    bext.clear()

    logos = []
    for i in range(NUMBER_OF_LOGOS):
        logos.append({COLOR: random.choice(COLORS),
                      X: random.randint(1, WIDTH - len(WORD) - 1),
                      Y: random.randint(1, HEIGHT - len(WORD) - 1),
                      DIR: random.choice(DIRECTIONS)})
        if logos[-1][X] % 2 == 1:
            logos[-1][X] -= 1

    corner_bounces = 0
    while True:
        for logo in logos:
            bext.goto(logo[X], logo[Y])
            print(' '*len(WORD), end='', flush = True)

            original_direction = logo[DIR]

            if logo[X] == 0 and logo[Y] == 0:
                logo[DIR] = DOWN_RIGHT
                corner_bounces += 1
            elif logo[X] == 0 and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_RIGHT
                corner_bounces += 1
            elif logo[X] == WIDTH - len(WORD) and logo[Y] == 0:
                logo[DIR] = DOWN_LEFT
                corner_bounces += 1
            elif logo[X] == WIDTH - len(WORD) and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_LEFT
                corner_bounces += 1

            elif logo[X] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = UP_RIGHT
            elif logo[X] == 0 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = DOWN_RIGHT

            elif logo[X] == WIDTH - len(WORD) and logo[DIR] == UP_RIGHT:
                logo[DIR] = UP_LEFT
            elif logo[X] == WIDTH - len(WORD) and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = DOWN_LEFT

            elif logo[Y] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = DOWN_LEFT
            elif logo[Y] == 0 and logo[DIR] == UP_RIGHT:
                logo[DIR] = DOWN_RIGHT

            elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = UP_LEFT
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = UP_RIGHT

            if logo[DIR] != original_direction:
                logo[COLOR] = random.choice(COLORS)

            if logo[DIR] == UP_RIGHT:
                logo[X] += 2
                logo[Y] -= 1
            elif logo[DIR] == UP_LEFT:
                logo[X] -= 2
                logo[Y] -= 1
            elif logo[DIR] == DOWN_RIGHT:
                logo[X] += 2
                logo[Y] += 1
            elif logo[DIR] == DOWN_LEFT:
                logo[X] -= 2
                logo[Y] += 1

        bext.goto(5, 0)
        bext.fg('white')
        print('Bounce of the corner: ', corner_bounces, end=' ')

        for logo in logos:
            bext.goto(logo[X], logo[Y])
            bext.fg(logo[COLOR])
            print(WORD, end=' ')

        bext.goto(0,0)

        sys.stdout.flush()
        time.sleep(PAUSE_AMOUNT)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Animation')
        sys.exit()