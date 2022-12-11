import os

dir = os.path.dirname(__file__)
f = open(dir + '/input.XSCORE.txt', 'r')


class Monkey:
    def __init__(self, id):
        self.id = id
        self.operation = 'old'
        self.if_true = self.id
        self.if_false = self.id
        self.test = 0
        self.items = []
        self.inspections = 0

    def __repr__(self):
        return '{\n\t' + str(self.id) + ',\n\t' + self.operation + ',\n\t' + str(self.if_true) + ',\n\t' + str(self.if_false) + ',\n\t' + str(self.inspections) + ',\n\t' + str(self.items) + '\n\t' + str(self.test) + '\n}'


def parse_monkey(f):
    global lcm
    monkey = ''
    while True:
        line = f.readline().replace('\n', '')
        if line == '':
            return monkey

        expression = line.replace('\n', '').replace('  ', '').split(': ')

        action = expression[0].replace(':', '').split(' ')

        match (action[0]):
            case 'Monkey':
                monkey = Monkey(int(action[1]))
            case 'Starting':
                items = [int(x) for x in expression[1].split(', ')]
                for item in items:
                    monkey.items.append(item)
            case 'Operation':
                monkey.operation = expression[1].split(' = ')[1]
            case 'Test':
                monkey.test = int(expression[1].split(' ')[2])
                lcm *= monkey.test
            case 'If':
                if action[1] == 'true':
                    monkey.if_true = int(expression[1].split(' ')[3])
                else:
                    monkey.if_false = int(expression[1].split(' ')[3])


monkeys = []
lcm = 1

while True:
    monkey = parse_monkey(f)
    if monkey == '':
        break

    monkeys.append(monkey)

for round in range(10000):
    for monkey in monkeys:
        for i in range(len(monkey.items)):
            monkey.inspections += 1
            old = monkey.items.pop()
            new = eval(monkey.operation) % lcm

            if new % monkey.test == 0:
                monkeys[monkey.if_true].items.append(new)
            else:
                monkeys[monkey.if_false].items.append(new)

monkeys.sort(key=lambda x: x.inspections, reverse=True)
print(monkeys[0].inspections * monkeys[1].inspections)
