import os

dir = os.path.dirname(__file__)
f = open(dir + '/input.XSCORE.txt', 'r')

points = 0

def calculate_points(a, x):
    round_points = 0

    match (x):
        case 'X':
            round_points += 1
        case 'Y':
            round_points += 2
        case 'Z':
            round_points += 3

    match (a+x):
        case 'AX':
            round_points += 3
        case 'AY':
            round_points += 6
        case 'AZ':
            round_points += 0
        case 'BX':
            round_points += 0
        case 'BY':
            round_points += 3
        case 'BZ':
            round_points += 6
        case 'CX':
            round_points += 6
        case 'CY':
            round_points += 0
        case 'CZ':
            round_points += 3

    return round_points
    

while True:
    round = f.readline()
    if round == '':
        break
    
    [a, x] = round.replace('\n', '').split(' ', 2)
    points += calculate_points(a, x)

print(points)
