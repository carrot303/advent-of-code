from collections import defaultdict
from itertools import combinations

input = """
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""

with open("input_day8.txt") as file: input = file.read()

map = [list(i) for i in input.strip().split("\n")]
antennas_coords = defaultdict(list)

for r in range(len(map)):
	for c in range(len(map[r])):
		(map[r][c] != "."
		and antennas_coords[map[r][c]].append((r,c)))


def inbound(r, c):
	return r >= 0 and r < len(map) and c >= 0 and c < len(map[0])


def map_signal(comb, antinodes, limit=1):
	def line(coord, dis):
		l = limit
		t = coord
		r = t[0]+dis[0]
		c = t[1]+dis[1]
		while l > 0:
			r = t[0]+dis[0]
			c = t[1]+dis[1]
			if not inbound(r, c): break
			t = (r, c)
			if map[r][c] == ".":
				map[r][c] = "#"
			antinodes.add(t)
			l -= 1

	a1, a2 = comb
	if limit == float("inf"):
		antinodes.add(a1)
		antinodes.add(a2)

	d1 = a1[0]-a2[0], a1[1]-a2[1]
	d2 = a2[0]-a1[0], a2[1]-a1[1]
	line(a1, d1)
	line(a2, d2)


def part1():
	antinodes = set()
	for antenna in antennas_coords:
		coords = antennas_coords[antenna]
		combs = combinations(coords, 2)
		for comb in combs:
			map_signal(comb, antinodes)
	return len(antinodes)


def part2():
	antinodes = set()
	for antenna in antennas_coords:
		coords = antennas_coords[antenna]
		combs = combinations(coords, 2)
		for comb in combs:
			map_signal(comb, antinodes, limit=float("inf"))
	return len(antinodes)



print("Part 1:", part1())
print("Part 2:", part2())
