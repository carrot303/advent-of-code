input = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

# with open("input_day6.txt") as file: input = file.read()

mmap = [list(line) for line in input.strip().split("\n")]

l = len(mmap[0])
y_guard = input.strip().find("^")//(l+1)
x_guard = input.strip().find("^")%(l+1)

steps = []
dir_steps = []
blocks = []
direction = ["up", "right", "down", "left"]
direction_movement = [(-1, 0), (0, 1), (1, 0), (0, -1)]
obs = 0
steps_count = 0

# not efficient
blocks_according_to_dir = {
	"up": (
		lambda s: [b for b in blocks if b[0] == s[0] and b[1] > s[1]],
		lambda s: [b for b in blocks if b[1] == s[1] and b[0] > s[0]],
	),
	"right": (
		lambda s: [b for b in blocks if b[0] == s[0] and b[1] < s[1]],
		lambda s: [b for b in blocks if b[1] == s[1] and b[0] > s[0]],
	),
	"down": (
		lambda s: [b for b in blocks if b[0] == s[0] and b[1] < s[1]],
		lambda s: [b for b in blocks if b[1] == s[1] and b[0] < s[0]],
	),
	"left": (
		lambda s: [b for b in blocks if b[0] == s[0] and b[1] > s[1]],
		lambda s: [b for b in blocks if b[1] == s[1] and b[0] < s[0]],
	),
}

def loop_possible(step, dir):
	h = blocks_according_to_dir[dir][0](step)
	v = blocks_according_to_dir[dir][1](step)
	for i in h:
		for j in v:
			py = step[0] ^ i[0] ^ j[0]
			px = step[1] ^ i[1] ^ j[1]
			if (py, px) in blocks:
				print(step, i, j, (py,px), dir)


while True:
	idx = obs % len(direction)
	cdir = direction[idx]
	ychange, xchange = direction_movement[idx]
	if y_guard+ychange >= len(mmap) or x_guard+xchange >= len(mmap[0]):
		break
	if mmap[y_guard+ychange][x_guard+xchange] == "#":
		blocks.append((y_guard,x_guard))
		obs += 1
		continue
	y_guard += ychange
	x_guard += xchange
	if not (y_guard,x_guard) in steps: steps_count += 1
	steps.append((y_guard,x_guard))
	dir_steps.append(cdir)


for i in range(len(steps)):
	loop_possible(steps[i], dir_steps[i])


print("Part 1:", steps_count)
