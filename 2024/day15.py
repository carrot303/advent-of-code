_input = input
input = """
##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
"""

with open("input_day15.txt") as file: input = file.read()


grid = [list(l) for l in input.strip().split("\n\n")[0].split("\n")]
moves = input.strip().split("\n\n")[1].replace("\n", "")
for i in range(len(grid)):
	for j in range(len(grid[0])):
		if grid[i][j] == "@":
			ROBOT_Y = i
			ROBOT_X = j
			break
	else:
		continue
	break


directions = {
	"<": (0, -1),
	">": (0, +1),
	"v": (+1, 0),
	"^": (-1, 0),
}

def do_move(d, robot_y, robot_x):
	dy, dx = directions[d]
	y, x = robot_y+dy, robot_x+dx
	cnt = 0
	block = False
	if grid[y][x] == "#":
		return ROBOT_Y, ROBOT_X
	elif grid[y][x] == "O":
		ty, tx = y, x
		cnt = 0
		while grid[ty][tx] == "O":
			if grid[ty+dy][tx+dx] == "#":
				block = True
				break
			ty += dy
			tx += dx
			cnt += 1

	reverse_y, reverse_x = -dy, -dx
	if cnt and grid[ty][tx] == ".":
		for i in range(cnt):
			grid[ty][tx] = "O"
			ty += reverse_y
			tx += reverse_x

	if not block:
		grid[y][x] = "@"
		grid[robot_y][robot_x] = "."
		return y, x
	return robot_y, robot_x


for move in moves:
	ROBOT_Y, ROBOT_X = do_move(move, ROBOT_Y, ROBOT_X)


p1 = 0
for i in range(len(grid)):
	for j in range(len(grid[0])):
		if grid[i][j] == "O":
			p1 += 100 *  i + j

print("Part 1:", p1)