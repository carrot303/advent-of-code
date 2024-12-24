from collections import defaultdict
import copy

_input = input

input = """
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
"""

with open("input_day12.txt") as file: input = file.read()


map = [list(i) for i in input.strip().split("\n")]

lrow = len(map)
lcol = len(map[0])
visited = defaultdict(bool)
directions = [(1,0),(-1,0),(0,1),(0,-1)]
dir_symbols = "BTRL"
inside_vertices = {
	"TL": (-1, -1),
	"TR": (-1, 1),
	"BL": (1, -1),
	"BR": (1, 1),
}


def inbound(row, col):
	return 0 <= row < lrow and 0 <= col < lcol


def get_shape(row, col, points):
	letters = map[row][col]
	visited[(row, col)] = letters
	points.append((row, col))
	for r, c in directions:
		if (inbound(row+r, col+c)
			and not visited[(row+r, col+c)]
			and map[row+r][col+c] == letters):
			get_shape(row+r, col+c, points)
	return points


def get_neighboors(point, points):
	neighboors = 0
	ns = ""
	for r, c in directions:
		if (point[0]+r, point[1]+c) in points:
			neighboors += 1
			ns += dir_symbols[directions.index((r, c))]
	return neighboors, ns



part1 = 0
part2 = 0
for i in range(lrow):
	for j in range(lcol):
		if map[i][j] == "." or visited[(i, j)]:
			continue
		points = get_shape(i, j, [])
		perimiter = 0
		corners = 0
		letter = map[i][j]
		for p in points:
			pr,pc = p
			nc, ns = get_neighboors(p, points)
			perimiter += 4 - nc
			if ns in ["BR", "TR", "TL", "BL"]:
				corners += 1
			if ns in ["B", "R", "T", "L"]:
				corners += 2
			for iv in inside_vertices:
				tr, tc = inside_vertices[iv]
				if (iv[0] in ns and iv[1] in ns
					and map[pr+tr][pc+tc] != letter):
					corners += 1

		part1 += len(points) * perimiter
		part2 += len(points) * max(4, corners)

print("Part 1:", part1)
print("Part 2:", part2)