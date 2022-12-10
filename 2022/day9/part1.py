import os

dir = os.path.dirname(__file__)
f = open(dir + '/input.XSCORE.txt', 'r')


def get_new_t(t, new_h):
    diff = [new_h[0] - t[0], new_h[1] - t[1]]

    match ([abs(diff[0]), abs(diff[1])]):
        case [0, 0]:
            return t
        case [0, 1]:
            return t
        case [1, 0]:
            return t
        case [1, 1]:
            return t
        case [2, 0]:
            return [t[0] + int(diff[0] / 2), t[1]]
        case [0, 2]:
            return [t[0], t[1] + int(diff[1] / 2)]
        case [2, 1]:
            return [t[0] + int(diff[0] / 2), t[1] + diff[1]]
        case [1, 2]:
            return [t[0] + diff[0], t[1] + int(diff[1] / 2)]


h = [0, 0]
t = [0, 0]
t_positions = []

while True:
    line = f.readline()
    if line == '':
        break
    movement = line.replace('\n', '').split(' ')
    [direction, delta] = [movement[0], int(movement[1])]

    for i in range(delta):
        match (direction):
            case 'U':
                new_h = [h[0], h[1] + 1]
            case 'D':
                new_h = [h[0], h[1] - 1]
            case 'L':
                new_h = [h[0] - 1, h[1]]
            case 'R':
                new_h = [h[0] + 1, h[1]]

        t = get_new_t(t, new_h)
        if t not in t_positions:
            t_positions.append(t)
        h = new_h


print(len(t_positions))
