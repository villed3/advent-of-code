import os

dir = os.path.dirname(__file__)
f = open(dir + '/input.XSCORE.txt', 'r')


def print_screen(screen):
    for i in range(len(screen)):
        if i % 40 == 0:
            print('')
        print(screen[i], end='')


instructions = [['addx', 2], ['noop', 1]]

cycle = 0
prev_instr = []
wait = 0
to_add = 0
x = 1
screen = ['.']*240

while True:
    if cycle % 40 in range(x - 1, x + 2):
        screen[cycle % 240] = '#'
    else:
        screen[cycle % 240] = '.'

    cycle += 1

    if wait == 0:
        line = f.readline()
        if line == '':
            break
        instr = line.replace('\n', '').split(' ')

        match (instr[0]):
            case 'addx':
                prev_instr = instr
                wait = 2
            case 'noop':
                prev_instr = instr
                wait = 1
    elif wait == 1 and prev_instr[0] == 'addx':
        to_add = int(prev_instr[1])

    if to_add != 0:
        x += to_add
        to_add = 0

    wait -= 1

print_screen(screen)
