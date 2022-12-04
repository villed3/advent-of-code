import os

dir = os.path.dirname(__file__)
f = open(dir + '/input.XSCORE.txt', 'r')

overlap_count = 0

while True:
    line = f.readline()
    if line == '':
        break

    [a1, a2, b1, b2] = line.replace('-', ',').split(',')
    r1 = range(int(a1), int(a2) + 1)
    r2 = range(int(b1), int(b2) + 1)

    if r1.start in r2 or r2.start in r1:
        overlap_count += 1


print(overlap_count)
