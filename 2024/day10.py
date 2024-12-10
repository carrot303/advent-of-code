from collections import defaultdict
import copy

input = """
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""

with open("input_day10.txt") as file: input = file.read()


gmap = [list(map(int, i)) for i in input.strip().split("\n")]
row_count = len(gmap)
col_count = len(gmap[0])

hicking_trails = defaultdict(set)
hicking_trails_rates = defaultdict(int)


def hicking(tailhead, row, col):
	if gmap[row][col] == 9:
		hicking_trails_rates[tailhead] += 1
		hicking_trails[tailhead].add((row, col))
		return None

	current = (row, col)
	next_height = gmap[row][col]+1
	if row+1 < row_count and gmap[row+1][col] == next_height:
		hicking(tailhead, row+1, col)
	if row-1 >= 0 and gmap[row-1][col] == next_height:
		hicking(tailhead, row-1, col)
	if col+1 < col_count and gmap[row][col+1] == next_height:
		hicking(tailhead, row, col+1)
	if col-1 >= 0 and gmap[row][col-1] == next_height:
		hicking(tailhead, row, col-1)

whole_score = 0
rate = 0
for r in range(len(gmap)):
	for c in range(len(gmap[r])):
		if gmap[r][c] == 0:
			hicking((r,c), r, c)
			score = len(hicking_trails[(r, c)])
			whole_score += score
			rate += hicking_trails_rates[(r, c)]

print("Part 1:", whole_score)
print("Part 2:", rate)
