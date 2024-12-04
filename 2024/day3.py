import re

input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
with open("input_day3.txt") as file: input = file.read()


mul_pattern = re.compile(r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\)")


mul_enabled = True

result1 = 0
result2 = 0

for expr in mul_pattern.findall(input):
	if expr.startswith("mul"):
		x, y = [int(n) for n in expr[4:-1].split(",")]
		result1 += x * y
		if mul_enabled:
			result2 += x * y
	elif expr == "don't()":
		mul_enabled = False
	elif expr == "do()":
		mul_enabled = True


print("Part 1:", result1)
print("Part 2:", result2)
