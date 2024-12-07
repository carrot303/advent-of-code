import itertools


input = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""

with open("input_day7.txt") as file: input = file.read()


def cal(f, lst, ops):
	ps = itertools.product(ops, repeat=len(lst)-1)

	for p in ps:
		lp = list(p)
		op = lp.pop(0)
		if op == "*":
			res = lst[0] * lst[1]
		elif op == "+":
			res = lst[0] + lst[1]
		else:
			res = int(str(lst[0]) + str(lst[1]))

		for num in lst[2:]:
			op = lp.pop(0)
			if op == "*":
				res *= num
			elif op == "+":
				res += num
			else:
				res = int(str(res) + str(num))
		if res == f:
			return True

	return False


def part1():
	cnt = 0
	for line in input.strip().split("\n"):
		result, *numbers = [int(i) for i in line.replace(":", "").split(" ")]
		if cal(result, numbers, "+*"): cnt += result
	return cnt


def part2():
	cnt = 0
	for line in input.strip().split("\n"):
		result, *numbers = [int(i) for i in line.replace(":", "").split(" ")]
		if cal(result, numbers, "+*|"): cnt += result
	return cnt


print("Part 1:", part1())
print("Part 2:", part2())