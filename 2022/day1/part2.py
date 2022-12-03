import os

dir = os.path.dirname(__file__)
f = open(dir + '/input.XSCORE.txt', 'r')
maxs = [0, 0, 0]
currentNumber = ''
currentTotal = 0

while True:
    char = f.read(1)

    if char == '':
        break

    elif char.isnumeric():
        currentNumber += char

    elif char == '\n':
        currentTotal += int(currentNumber)
        currentNumber = ''
        char = f.read(1)

        if char == '\n':
            for m in maxs:
                if currentTotal > m:
                    maxs[2] = currentTotal
                    maxs.sort(reverse=True)
                    break
            currentTotal = 0

        elif char.isnumeric():
            currentNumber += char

print('Max number is: ')
print(maxs[0] + maxs[1] + maxs[2])
