import os

dir = os.path.dirname(__file__)
f = open(dir + '/input.XSCORE.txt', 'r')


def get_new_pos(knot, prev):
    diff = [prev[0] - knot[0], prev[1] - knot[1]]

    match ([abs(diff[0]), abs(diff[1])]):
        case [0, 0]:
            return knot
        case [0, 1]:
            return knot
        case [1, 0]:
            return knot
        case [1, 1]:
            return knot
        case [2, 0]:
            return [knot[0] + int(diff[0] / 2), knot[1]]
        case [0, 2]:
            return [knot[0], knot[1] + int(diff[1] / 2)]
        case [2, 1]:
            return [knot[0] + int(diff[0] / 2), knot[1] + diff[1]]
        case [1, 2]:
            return [knot[0] + diff[0], knot[1] + int(diff[1] / 2)]
        case [2, 2]:
            return [knot[0] + int(diff[0] / 2), knot[1] + int(diff[1] / 2)]


rope_length = 10
rope = [[0, 0] for _ in range(rope_length)]

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
                new_h = [rope[0][0], rope[0][1] + 1]
            case 'D':
                new_h = [rope[0][0], rope[0][1] - 1]
            case 'L':
                new_h = [rope[0][0] - 1, rope[0][1]]
            case 'R':
                new_h = [rope[0][0] + 1, rope[0][1]]

        prev = new_h

        for i in range(1, rope_length):
            knot = get_new_pos(rope[i], prev)
            if i == 9 and knot not in t_positions:
                t_positions.append(knot)
            rope[i] = prev = knot

        rope[0] = new_h

print(len(t_positions))
