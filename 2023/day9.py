
with open("inputs/day9.txt") as file:
	puzzle = file.read().strip()

result = 0
result2 = 0


for history in puzzle.split("\n"):
	numbers = [int(i) for i in history.split()]
	temp = [i for i in numbers]
	temps = []
	while temp.count(0) != len(temp):
		temps.append(temp)
		f, *rest = temp
		temp = []
		for i in rest:
			temp.append(i - f)
			f = i
	temps.append(temp)

	# Part one
	r = 0
	for i in range(len(temps)):
		r += temps[i][-1]
	result += r

	# Part two
	r2 = 0
	for i in range(len(temps)-2, -1, -1):
		r2 = temps[i][0] - r2
	result2 += r2

print("Part one:", result)
print("Part two:", result2)