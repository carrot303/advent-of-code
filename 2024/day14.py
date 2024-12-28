from collections import defaultdict
import copy

input = """
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
"""

with open("input_day14.txt") as file: input = file.read()


robots = input.strip().split("\n")
robots_info = []

for r in robots:
	p, v = r.split()
	py, px = map(int, p[2:].split(","))
	vy, vx = map(int, v[2:].split(","))
	robots_info.append(((py, px), (vy, vx)))


wide = max(robots_info, key=lambda x: x[0][0])[0][0]+1
tall = max(robots_info, key=lambda x: x[0][1])[0][1]+1
tiles = [[0 for _ in range(wide)] for _ in range(tall)]
char_tiles = [["." for _ in range(wide)] for _ in range(tall)]




def elapse_seconds(seconds=100, shaped=False):
	ttiles = copy.deepcopy(char_tiles) if shaped else copy.deepcopy(tiles)
	for ri in robots_info:
		p1, p2 = ri[0]
		v1, v2 = ri[1]
		n1, n2 = (p1+(seconds*v1))%wide, (p2+(seconds*v2))%tall
		if shaped:
			ttiles[n2][n1] = "@"
		else:
			ttiles[n2][n1] += 1

	return ttiles


def part1():
	ttiles = elapse_seconds(100)
	q = 0
	res = defaultdict(int)
	for i in range(len(ttiles)):
		c1, c2 = ttiles[i][:wide//2], ttiles[i][(wide//2)+1:]
		if i==tall//2:
			q = 1
			continue
		res[(q,0)] += sum(c1) 
		res[(q,1)] += sum(c2) 

	p1 = 1
	for i in res.values():
		p1 *= i
	return p1


def part2():
	sec = 0
	while True:
		sec += 1
		ttiles = elapse_seconds(sec, True)
		for i in ttiles:
			if "@@@@@@@@@@@@" in "".join(i):
				return sec
	return sec


print("Part 1:", part1())
print("Part 2:", part2())