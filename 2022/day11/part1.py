import os
import queue
import operator

dir = os.path.dirname(__file__)
f = open(dir + '/input.XSCORE.txt', 'r')


class Monkey:
    def __init__(self, id):
        self.id = id
        self.operation = 'old'
        self.if_true = self.id
        self.if_false = self.id
        self.test = 0
        self.items = queue.Queue()
        self.inspections = 0

    def __repr__(self):
        return '{\n\t' + str(self.id) + ',\n\t' + self.operation + ',\n\t' + str(self.if_true) + ',\n\t' + str(self.if_false) + ',\n\t' + str(self.inspections) + ',\n\t' + str(self.items.queue) + '\n\t' + str(self.test) + '\n}'


def parse_monkey(f):
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
                    monkey.items.put(item)
            case 'Operation':
                monkey.operation = expression[1].split(' = ')[1]
            case 'Test':
                monkey.test = int(expression[1].split(' ')[2])
            case 'If':
                if action[1] == 'true':
                    monkey.if_true = int(expression[1].split(' ')[3])
                else:
                    monkey.if_false = int(expression[1].split(' ')[3])


monkeys = []

while True:
    monkey = parse_monkey(f)
    if monkey == '':
        break

    monkeys.append(monkey)

for round in range(20):
    for monkey in monkeys:
        for i in range(monkey.items.qsize()):
            monkey.inspections += 1
            old = monkey.items.get()
            new = eval(monkey.operation) // 3

            if new % monkey.test == 0:
                monkeys[monkey.if_true].items.put(new)
            else:
                monkeys[monkey.if_false].items.put(new)


monkeys.sort(key=lambda x: x.inspections, reverse=True)
print(monkeys[0].inspections * monkeys[1].inspections)
