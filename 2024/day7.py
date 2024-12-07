
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


def valid(target, numbers, cat=False):
	if len(numbers) == 1:
		return target == numbers[0]
	if valid(target, [numbers[0]+numbers[1]]+numbers[2:], cat):
		return True
	if valid(target, [numbers[0]*numbers[1]]+numbers[2:], cat):
		return True
	if cat and valid(target, [int(str(numbers[0])+str(numbers[1]))]+numbers[2:], cat):
		return True
	return False


def part1():
	cnt = 0
	for line in input.strip().split("\n"):
		result, *numbers = [int(i) for i in line.replace(":", "").split(" ")]
		if valid(result, numbers):
			cnt += result
	return cnt


def part2():
	cnt = 0
	for line in input.strip().split("\n"):
		result, *numbers = [int(i) for i in line.replace(":", "").split(" ")]
		if valid(result, numbers, True):
			cnt += result
	return cnt


print("Part 1:", part1())
print("Part 2:", part2())