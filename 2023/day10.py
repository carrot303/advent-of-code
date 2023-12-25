with open("inputs/day10.txt") as file:
	puzzle = file.read().strip()

board = puzzle.split("\n")
start_position = None
found = False
for row in range(len(board)):
	for col in range(len(board[row])):
		if board[row][col] == "S":
			start_position = (row, col)
			found = True
			break
	if found:
		break


ENTER_DIRECTIONS = {"F": ["D", "R"],"L": ["U", "R"],"J": ["L", "U"],"7": ["D", "L"],"-": ["R", "L"],"|": ["U", "D"]}


def get_s_band(start_position):
	i, j = start_position
	r,l,u,d = "0","0","0","0"

	if j < len(board[0])-1:
		r = board[i][j+1]
	if j > 0:
		l = board[i][j-1]
	if i < len(board)-1:
		d = board[i+1][j]
	if i > 0:
		u = board[i-1][j]

	if r in "-J7" and d in "LJ|":
		return "F"
	elif r in "-J7" and u in "F7|":
		return "L"
	elif u in "F7|" and l in "F-L":
		return "J"
	elif d in "LJ|" and l in "F-L":
		return "7"
	elif r in "-J7" and l in "F-L":
		return "-"
	elif u in "F7|" and d in "LJ|":
		return "|"


def go_away(row, col, enter):
	pipe = board[row][col]
	i, j = row, col
	if pipe == "F" and enter == "R":
		row += 1
		enter = "U"
	elif pipe == "F" and enter == "D":
		col += 1
		enter = "L"
	elif pipe == "7" and enter == "D":
		col -= 1
		enter = "R"
	elif pipe == "7" and enter == "L":
		row += 1
		enter = "U"
	elif pipe == "J" and enter == "L":
		row -= 1
		enter = "D"
	elif pipe == "J" and enter == "U":
		col -= 1
		enter = "R"
	elif pipe == "L" and enter == "U":
		col += 1
		enter = "L"
	elif pipe == "L" and enter == "R":
		row -= 1
		enter = "D"
	elif pipe == "-" and enter == "R":
		col -= 1
	elif pipe == "-" and enter == "L":
		col += 1
	elif pipe == "|" and enter == "U":
		row += 1
	elif pipe == "|" and enter == "D":
		row -= 1

	if row == start_position[0] and col == start_position[1]:
		return False, row, col, enter
	if i == row and j == col:
		return False, False, False, False

	return True, row, col, enter


# Part one
step = 0
S_band = get_s_band(start_position)
i1, j1, enter1 = *start_position, ENTER_DIRECTIONS[S_band][0]
i2, j2, enter2 = *start_position, ENTER_DIRECTIONS[S_band][1]

res1 = True
res2 = True

board[i1] = board[i1].replace("S",S_band)
while res1 or res2:
	res1, i1, j1, enter1 = go_away(i1, j1, enter1)
	res2, i2, j2, enter2 = go_away(i2, j2, enter2)
	step += 1	
	if i1 == i2 and j1 == j2:
		break

print("Part one:", step)


# Part two (ray-casting-algorithm)
import sys

_huge = sys.float_info.max
_eps = 0.00001

def edges(points):
	e = []
	for i in range(len(points)):
		p1 = points[i]
		p2 = points[(i+1) % len(points)]
		e.append((p1,p2))
	return e


def is_inside(p):
	result = False
	p = [p[0],p[1]]
	for edge in edges_list:
		a,b = edge
		if a[1] > b[1]:
			a,b = b,a
		if p[1] == a[1] or p[1] == b[1]:
			p[1] += _eps

		if (p[1] > b[1] or p[1] < a[1] or p[0] > max(a[0],b[0])):
			continue
		if p[0] < min(a[0], b[0]):
			result = not result
			continue

		try:
			m_edge = (b[1]-a[1])/(b[0]-a[0])
		except ZeroDivisionError:
			m_edge = _huge

		try:
			m_point = (p[1]-a[1])/(p[0]-a[0])
		except ZeroDivisionError:
			m_point = _huge

		if m_point >= m_edge:
			result = not result
			continue
	return result


# Make our polygon
i, j, enter = *start_position, ENTER_DIRECTIONS[S_band][0]
res = True
points = []
new_board = [["." for _ in range(len(board[0]))] for _ in range(len(board))]
while res:
	new_board[i][j] = "1"
	if board[i][j] in ["7","F","L","J"]:
		points.append((i,j))
	res, i, j, enter = go_away(i, j, enter)

edges_list = edges(points)
insides = 0
for i in range(len(new_board)):
	for j in range(len(new_board[0])):
		if new_board[i][j] == "." and is_inside((i,j)): # it's a point
			insides += 1

print("Part two:", insides)