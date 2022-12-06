import os

dir = os.path.dirname(__file__)
f = open(dir + '/input.XSCORE.txt', 'r')

distinct_chars = 14

buffer = f.readline()

last_four = ['' for _ in range(distinct_chars)]

for i in range(0, len(buffer)):
	last_four[i % distinct_chars] = buffer[i]
	unique = set(filter(None, last_four))
	if len(unique) == distinct_chars:
		print(i + 1)
		break