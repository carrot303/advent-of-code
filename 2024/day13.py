import re

input = """
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""

with open("input_day13.txt") as file: input = file.read()


def solve(offset=0):
	r = 0
	for i in input.strip().split("\n\n"):
		b1, b2, p = i.split("\n")
		x1, y1 = [int(k) for k in re.findall(r"\d+", b1)]
		x2, y2 = [int(k) for k in re.findall(r"\d+", b2)]
		px, py = [int(k)+offset for k in re.findall(r"\d+", p)]
		# for part two (only append px,py to 10000000000000)
		X = ((px*y2)-(py*x2))/((x1*y2)-(x2*y1))
		Y = ((x1*py)-(y1*px))/((x1*y2)-(x2*y1))
		if int(X) != X or int(Y) != Y:
			continue
		r += int(X)*3+int(Y)
	return r

print("Part 1:", solve())
print("Part 2:", solve(10000000000000))