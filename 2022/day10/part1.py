import os

dir = os.path.dirname(__file__)
f = open(dir + '/input.XSCORE.txt', 'r')

stops = [20, 60, 100, 140, 180, 220]

instructions = [['addx', 2], ['noop', 1]]

cycle = 0
prev_instr = []
wait = 0
to_add = 0
x = 1
values = []
	
while True:
	cycle += 1

	if wait == 0:
		line = f.readline()
		if line == '':
			break
		instr = line.replace('\n', '').split(' ')

		match (instr[0]):
			case 'addx':
				prev_instr = instr
				wait = 2
			case 'noop':
				prev_instr = instr
				wait = 1
	elif wait == 1 and prev_instr[0] == 'addx':
		to_add = int(prev_instr[1])
	
	if cycle in stops:
		values.append(x * cycle)

	if to_add != 0:
		x += to_add
		to_add = 0

	wait -= 1
	

print(sum(values))

