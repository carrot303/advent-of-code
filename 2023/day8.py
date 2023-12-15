import time

with open("inputs/day8.txt") as file:
	puzzle = file.read().strip()


instruction, _, *rest = puzzle.split("\n")

maps = {}
for i in rest:
	n, d = i.split("=")
	d = d.replace("(", "").replace(")", "").replace(" ", "").split(",")
	maps[n.strip()] = d

node = "AAA"

i = 0
c = 0

while node != "ZZZ":
	if i == len(instruction):
		i = 0
	node = maps[node][0 if instruction[i] == "L" else 1]
	i += 1
	c += 1

print(c)