import sys

input = "125 17"
with open("input_day11.txt") as file: input = file.read()

stones = [int(i) for i in input.strip().split()]
dp = {}


def blink(stone, times):

	if (stone, times) in dp:
		return dp[(stone, times)]

	if times <= 0:
		return [stone]

	if stone == 0:
		return blink(1, times-1)
	elif len(str(stone)) % 2 == 0:
		l = len(str(stone))
		h1, h2 = int(str(stone)[:l//2]), int(str(stone)[l//2:])		
		return blink(h1, times-1) + blink(h2, times-1)
	else:
		return blink(stone*2024, times-1)


p1 = 0
for s in stones:
	a = blink(s, int(sys.argv[1]))
	p1 += len(a)

print("Part 1:", p1)