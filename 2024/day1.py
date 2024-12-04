input = """
3   4
4   3
2   5
1   3
3   9
3   3
"""

with open("input_day1.txt") as file: input = file.read()

left = []
right = []
for i in input.strip().split("\n"):
	right.append(i.split(" ")[-1])
	left.append(i.split(" ")[0])


left.sort()
right.sort()

result1 = 0
for l,r in zip(left, right):
	result1 += abs(int(l)-int(r))

result2 = 0
for l in left:
	result2 += int(l) * right.count(l)


print("Part 1:", result1)
print("Part 2:", result2)
