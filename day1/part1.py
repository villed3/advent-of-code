import os

dir = os.path.dirname(__file__)
f = open(dir + '/input.XSCORE.txt', 'r')
max = 0
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
            if currentTotal > max:
                max = currentTotal
            currentTotal = 0

        elif char.isnumeric():
            currentNumber += char

print('Max number is: ')
print(max)