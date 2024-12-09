_input = input
input = """
....#.....
.........#
..........
..#.......
..#....#..
.......#..
.#..^.....
........#.
#.........
......#...
"""

# with open("input_day6.txt") as file: input = file.read()

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


def in_bound(row, col):
	return row >= 0 and row < len(mmap) and col >= 0 and col < len(mmap[0])


def walk(direction="up", row=row, col=col, set_obs=True):
	direction_index = directions.index(direction)
	visited_steps = [(["."] * len(mmap[i])) for i in range(len(mmap))]
	step_count = 0
	loops_count = 0
	while True:
		cdir = directions[direction_index%4]
		r, c = step_direction[cdir]
		if not in_bound(row+r, col+c): break
		if mmap[row+r][col+c] == "#":
			direction_index += 1
			continue

		row += r
		col += c
		if visited_steps[row][col] == cdir[0]:
			return step_count, True, loops_count
		step_count += visited_steps[row][col] == "."
		visited_steps[row][col] = cdir[0]
		if not set_obs:
			continue

		r, c = step_direction[cdir]
		if not in_bound(row+r, col+c): break
		if mmap[row+r][col+c] == "#": continue
		mmap[row+r][col+c] = "#"
		if walk(cdir, row, col, set_obs=False)[1]:
			loops_count += 1
			mmap[row+r][col+c] = "O"
		else:
			mmap[row+r][col+c] = "."

	return step_count, False, loops_count


step, _, count= walk(set_obs=True)
print("Part 1:", step)
print("Part 2:", count)
