import os
import queue
# list of input stacks, as strings, in file called input.py
import input

dir = os.path.dirname(__file__)
f = open(dir + '/input.XSCORE.txt', 'r')

initial_stacks = input.STACKS

stacks = []

for i in range(len(initial_stacks)):
    stack = queue.LifoQueue()
    for c in initial_stacks[i]:
        stack.put(c)
    stacks.append(stack)

while True:
    line = f.readline()
    if line == '':
        break

    [count, s1, s2] = map(int, line.replace('move ', '').replace(
        'from ', '').replace('to ', '').split())

    moved = queue.LifoQueue()

    for i in range(0, count):
        moved.put(stacks[s1 - 1].get())

    while not moved.empty():
        stacks[s2 - 1].put(moved.get())


top_items = ''

for i in range(len(stacks)):
    top_items += stacks[i].get()

print(top_items)
