import os

dir = os.path.dirname(__file__)
f = open(dir + '/input.XSCORE.txt', 'r')

total = 0

def calculate_priority(c):
    if c.islower():
        return ord(c) - 96
    else:
        return ord(c) - 38


while True:
    rucksack1 = f.readline().strip('\n')
    rucksack2 = f.readline().strip('\n')
    rucksack3 = f.readline().strip('\n')
    if rucksack1 == '':
        break

    for c1 in rucksack1:
        for c2 in rucksack2:
            for c3 in rucksack3:
                if c1 == c2 == c3:
                    c = c1

    total += calculate_priority(c)

print(total)
