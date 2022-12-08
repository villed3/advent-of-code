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


def count_visible(matrix):
    total = 0
    for row in matrix:
        for cell in row:
            total += cell
    return total


forest_matrix = parse_matrix(f)
x, y = len(forest_matrix[0]), len(forest_matrix)
visible_matrix = [[0 for _ in range(x)] for _ in range(y)]

# from top and bottom
for dx in range(x):
    # top
    visible_matrix[0][dx] = 1
    tallest = forest_matrix[0][dx]
    for dy in range(1, y):
        if forest_matrix[dy][dx] > tallest:
            tallest = forest_matrix[dy][dx]
            visible_matrix[dy][dx] = 1
    # bottom
    visible_matrix[y-1][dx] = 1
    tallest = forest_matrix[y-1][dx]
    for dy in range(1, y):
        if forest_matrix[y - dy - 1][dx] > tallest:
            tallest = forest_matrix[y - dy - 1][dx]
            visible_matrix[y - dy - 1][dx] = 1

# from left and right
for dy in range(y):
    # left
    visible_matrix[dy][0] = 1
    tallest = forest_matrix[dy][0]
    for dx in range(1, x):
        if forest_matrix[dy][dx] > tallest:
            tallest = forest_matrix[dy][dx]
            visible_matrix[dy][dx] = 1
    # right
    visible_matrix[dy][x-1] = 1
    tallest = forest_matrix[dy][x-1]
    for dx in range(1, x):
        if forest_matrix[dy][x - dx - 1] > tallest:
            tallest = forest_matrix[dy][x - dx - 1]
            visible_matrix[dy][x - dx - 1] = 1

print(count_visible(visible_matrix))
