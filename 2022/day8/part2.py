import os

dir = os.path.dirname(__file__)
f = open(dir + '/input.XSCORE.txt', 'r')


def parse_row(f):
    row = []
    while True:
        c = f.read(1)
        if not c:
            return None
        if c == '\n':
            return row
        elif c:
            row.append(int(c))


def parse_matrix(f):
    matrix = []
    while True:
        row = parse_row(f)
        if row:
            matrix.append(row)
        else:
            return matrix


forest_matrix = parse_matrix(f)
x, y = len(forest_matrix[0]), len(forest_matrix)
max_scenic_score = 0

for dx in range(x):
	for dy in range(y):
		t = b = l = r = 0
		for dt in range(1, dy + 1):
			t += 1
			if forest_matrix[dy - dt][dx] >= forest_matrix[dy][dx]:
				break
		for db in range(1, y - dy):
			b += 1
			if forest_matrix[dy + db][dx] >= forest_matrix[dy][dx]:
				break
		for dl in range(1, dx + 1):
			l += 1
			if forest_matrix[dy][dx - dl] >= forest_matrix[dy][dx]:
				break
		for dr in range(1, x - dx):
			r += 1
			if forest_matrix[dy][dx + dr] >= forest_matrix[dy][dx]:
				break
		scenic_score = t * b * l * r
		if scenic_score > max_scenic_score:
			max_scenic_score = scenic_score

print(max_scenic_score)