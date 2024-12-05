from collections import defaultdict
from functools import cmp_to_key


input = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""

with open("input_day5.txt") as file: input = file.read()


rules = defaultdict(list)
updates = []

for line in input.strip().split("\n"):
	if "|" in line:
		x,y = [int(i) for i in line.split("|")]
		rules[x].append(y)
	elif "," in line:
		numbers = [int(i) for i in line.split(",")]
		updates.append(numbers)


invalids = []
res1 = 0
for u in updates:
	valid = True
	for num in u:
		for xrule in rules[num]:
			if xrule in u and u.index(xrule) < u.index(num):
				valid = False
				break
		if not valid:
			break
	if valid:
		res1 += u[len(u)//2]
	else:
		invalids.append(u)


def sort(x, y):
	if y in rules[x]:
		return -1
	return 0

res2 = 0
for u in invalids:
	su = sorted(u, key=cmp_to_key(sort))
	res2 += su[len(su)//2]


print("Part 1:", res1)
print("Part 2:", res2)