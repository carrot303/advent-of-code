import copy
_input = input
input = """
....#...........
#...^....#......
..............#.
..#.............
#......#........
...........#....
.#..............
........#.......
#...........#...
...#..#..#....#
"""

with open("input_day6.txt") as file: input = file.read()

mmap = [list(line) for line in input.strip().split("\n")]

g_index = input.strip().find("^")
[(row, col)] = [(r,c) for r in range(len(mmap)) for c in range(len(mmap[r])) if mmap[r][c] == "^"]
directions = ["up", "right", "down", "left"]
step_direction = {
	"up": (-1, 0),
	"right": (0, 1),
	"down": (1, 0),
	"left": (0, -1)
}
steps = []


def in_bound(row, col):
	return row >= 0 and row < len(mmap) and col >= 0 and col < len(mmap[0])


def walk(direction="up", row=row, col=col, mark_steps=True):
	direction_index = directions.index(direction)
	visited_steps = [(["."] * len(mmap[i])) for i in range(len(mmap))]
	step_count = 0

	while True:
		cdir = directions[direction_index%4]
		r, c = step_direction[cdir]
		if not in_bound(row+r, col+c): break
		if mmap[row+r][col+c] == "#":
			direction_index += 1
			mark_steps and steps.append((row, col, directions[direction_index%4]))
			continue

		row += r
		col += c
		if visited_steps[row][col] == cdir[0]:
			return step_count, True
		step_count += visited_steps[row][col] == "."
		mark_steps and steps.append((row, col, cdir))
		visited_steps[row][col] = cdir[0]

	return step_count, False


step, _ = walk()
print("Part 1:", step)


# goes trough the guard's steps that taken
# check that placing an obstruction in front of guard is make a loop or not
loops = set()
for row, col, direction in steps:
	r,c = step_direction[direction]
	nr, nc = row+r, col+c
	if not in_bound(nr, nc):
		break

	# already has an obs in front of guard
	if mmap[nr][nc] == "#": continue

	# set temp obs
	mmap[nr][nc] = "#"
	_, looped = walk(direction, row, col, mark_steps=False)
	if looped:
		loops.add((nr,nc))

	# visualization (just for debug)
	mmap[nr][nc] = "."

print("Part 2:", len(loops))
