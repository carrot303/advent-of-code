
input = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

with open("input_day2.txt") as file: input = file.read()


result = 0
result2 = 0

def unsafe(lev1, lev2, sort):
	return (
		lev1 == lev2
		or (lev1 > lev2) != sort
		or abs(lev1-lev2) > 3
		or abs(lev1-lev2) < 1
	)

def is_safe(levels):
	if levels[0] == levels[1]: return False
	sort = levels[0] > levels[1]
	for l in range(len(levels)-1):
		if unsafe(levels[l], levels[l+1], sort):
			return False
	return True


for rep in input.strip().split("\n"):
	levels = [int(i) for i in rep.split()]
	if is_safe(levels):
		result += 1
	else:
		for l in range(len(levels)):
			copy_levels = levels[:l] + levels[l+1:]
			if is_safe(copy_levels):
				result2 += 1
				break

print("Part 1:", result)
print("Part 2:", result+result2)
