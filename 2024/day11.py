import copy
import sys
from collections import defaultdict, Counter

input = "125 17"
with open("input_day11.txt") as file: input = file.read()

stones = {int(i): 1 for i in input.strip().split()}
stones = defaultdict(int, stones)


def blink(temp):
	for k, v in stones.items():
		if temp[k] == 0: continue
		temp[k] -= v
		if k == 0:
			temp[1] += v
		elif len(str(k)) % 2 == 0:
			h1, h2 = int(str(k)[:len(str(k))//2]), int(str(k)[len(str(k))//2:])
			temp[h1] += v
			temp[h2] += v
		else:
			temp[k*2024] += v
	return temp

times = int(sys.argv[1])
for i in range(times):
	stones = blink(copy.deepcopy(stones))

c = Counter(stones)
print("Part 1:", c.total())