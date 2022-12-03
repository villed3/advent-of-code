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
    rucksack = f.readline().strip('\n')
    if rucksack == '': break

    compartment1 = rucksack[:len(rucksack)//2]
    compartment2 = rucksack[len(rucksack)//2:]

    for c1 in compartment1:
        for c2 in compartment2:
            if c1 == c2: c = c1
    
    total += calculate_priority(c)

print(total)