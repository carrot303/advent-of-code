from collections import defaultdict
_input = input
import copy

input = """
AAA
"""

with open("input_day12.txt") as file: input = file.read()


def space_between(lst):
	ll = list(lst)
	if type(lst) == str:
		l = ["." for i in range(len(ll)-1)]
	else:
		l = [["." for i in range(len(ll[0]))] for i in range(len(ll)-1)]
	c = []
	for i in range(len(ll)):
		c.append(ll.pop(0))
		l and c.append(l.pop(0))
	return c

map = []
for i in input.strip().split("\n"):
	d = copy.deepcopy(space_between(i))
	map.append(['.', '.'] + d + ['.', '.'])

map = space_between(map)
map.insert(0, ["." for i in range(len(map[0]))])
map.insert(0, ["." for i in range(len(map[0]))])
map.append(["." for i in range(len(map[0]))])
map.append(["." for i in range(len(map[0]))])


lrow = len(map)
lcol = len(map[0])
visited = {}
directions = [(2,0),(-2,0),(0,2),(0,-2)]
vertex_coords_offset = [(1, 1),(-1, -1), (1, -1), (-1, 1)]






def solve(row, col, vertexs, cnt=1):
	visited[(row, col)] = True
	plant = map[row][col]
	vertexs += [(row+vr, col+vc) for vr, vc in vertex_coords_offset]

	for r, c in directions:
		if map[row+r][col+c] == plant and (row+r, col+c) not in visited:
			_, cnt = solve(row+r, col+c, vertexs, cnt+1)

	return vertexs, cnt




p1 = 0
found = False
for i in range(lrow):
	for j in range(lcol):
		if map[i][j] == ".": continue
		if (i, j) in visited: continue

		vertexs, area = solve(i, j, [])
		found = True
		u_vertexs = set(vertexs)
		vs = [uv for uv in u_vertexs if vertexs.count(uv) < 4]
		traverse_perimeter(vs, vertexs)
		p1 += area*len(vs)
		break
	if found:
		break

for i in map:
	print("".join(i))
