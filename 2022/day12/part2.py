import os
import queue

dir = os.path.dirname(__file__)
f = open(dir + '/input.XSCORE.txt', 'r')


def find(char, heightmap):
    for y, row in enumerate(heightmap):
        for x, c in enumerate(row):
            if char == c:
                return [x, y]


input = f.read()

heightmap = []
for line in input.splitlines():
    row = []
    for c in line:
        row.append(c)
    heightmap.append(row)

[cols, rows] = [len(heightmap[0]), len(heightmap)]
visited = [[0 for _ in range(cols)] for _ in range(rows)]

start = find('S', heightmap)
end = find('E', heightmap)

heightmap[start[1]][start[0]] = 'a'
heightmap[end[1]][end[0]] = 'z'

que = queue.Queue()
move_count = 0
nodes_left_in_layer = 1
nodes_in_next_layer = 0

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

que.put(end)
# print(visited[end[1][end[0]]])
visited[end[1]][end[0]] = True

while que.qsize() > 0:
    [x, y] = que.get()

    if heightmap[y][x] == 'a':
        reached_end = True
        break
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]

        if new_x < 0 or new_y < 0:
            continue
        if new_x >= cols or new_y >= rows:
            continue
        if visited[new_y][new_x]:
            continue
        if ord(heightmap[y][x]) - ord(heightmap[new_y][new_x]) > 1:
            continue

        visited[new_y][new_x] = True
        nodes_in_next_layer += 1

        que.put([new_x, new_y])

    nodes_left_in_layer -= 1
    if nodes_left_in_layer == 0:
        nodes_left_in_layer = nodes_in_next_layer
        nodes_in_next_layer = 0
        move_count += 1


print(move_count)
