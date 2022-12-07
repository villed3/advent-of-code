import os
import queue

MAX_SIZE = 100000

dir = os.path.dirname(__file__)
f = open(dir + '/input.XSCORE.txt', 'r')

total_under_threshold = 0

class Directory:
	def __init__(self):
		self.subdirs = {}
		self.size_of_files = 0


def read_command(f):
	line: str = f.readline()
	if not line == '':
		return list(filter(None, line.replace('$', '').replace('\n', '').split(' ')))
	return


def read_until_command(f):
	res = ''
	while True:
		c = f.read(1)
		if c == '$' or c == '':
			break
		res += c
	return res

def get_current_dir(root, pwd):
	current_dir = root
	for e in pwd.queue:
		current_dir = current_dir.subdirs[e]
	return current_dir


def parse_ls(f, root, pwd):
	current_dir = get_current_dir(root, pwd)
	
	lines: str = read_until_command(f)
	if lines is None:
		return
	lines = lines.split('\n')

	size_of_files = 0
	for line in lines:
		if not ' ' in line:
			break
		[property, path] = line.split(' ')
		if property.isnumeric():
			size_of_files += int(property)
		elif property == 'dir' and path not in current_dir.subdirs:
			current_dir.subdirs[path] = Directory()

	current_dir.size_of_files = size_of_files

def calc_dir_size(dir):
	global total_under_threshold
	dir.size = dir.size_of_files
	for subdir in dir.subdirs:
		dir.size += calc_dir_size(dir.subdirs[subdir])
	if dir.size <= MAX_SIZE:
		total_under_threshold += dir.size
	return dir.size

root = Directory()
pwd = queue.LifoQueue()

while True:
	cmd = read_command(f)
	if not cmd: break

	match (cmd[0]):
		case 'cd':
			match (cmd[1]):
				case '/':
					pwd.queue.clear()
				case '..':
					pwd.get()
				case _:
					pwd.put(cmd[1])
		case 'ls':
			parse_ls(f, root, pwd)

calc_dir_size(root)

print(total_under_threshold)