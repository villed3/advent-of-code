import os

dir = os.path.dirname(__file__)
f = open(dir + '/input.XSCORE.txt', 'r')

points = 0

def calculate_points(a, x):
    round_points = 0

    match (x):
        case 'X':
            match (a):
                case 'A':
                    round_points += 3
                case 'B':
                    round_points += 1
                case 'C':
                    round_points += 2
        case 'Y':
            match (a):
                case 'A':
                    round_points += 1 + 3
                case 'B':
                    round_points += 2 + 3
                case 'C':
                    round_points += 3 + 3
        case 'Z':
            match (a):
                case 'A':
                    round_points += 2 + 6
                case 'B':
                    round_points += 3 + 6
                case 'C':
                    round_points += 1 + 6

    return round_points


while True:
    round = f.readline()
    if round == '':
        break

    [a, x] = round.replace('\n', '').split(' ', 2)
    points += calculate_points(a, x)

print(points)
