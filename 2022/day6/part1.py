import os

dir = os.path.dirname(__file__)
f = open(dir + '/input.XSCORE.txt', 'r')

buffer = f.readline()

last_four = ['', '', '', '']

for i in range(len(buffer)):
	last_four[i % 4] = buffer[i]
	unique = set(filter(None, last_four))
	if len(unique) == 4:
		print(i + 1)
		break
