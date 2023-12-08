with open("inputs/day6.txt") as file:
	puzzle = file.read().strip()


def beat(time, distance):
	for j in range(1, time):
		if (j*(time-j) > distance):
			break
	for q in range(time-1, j, -1):
		if (q*(time-q) > distance):
			break
	return abs(j-q)+1


times, distances = [list(map(int,nums.split()[1:])) for nums in puzzle.split("\n")]
result = 1
for i in range(len(times)):
	result *= beat(times[i], distances[i])

print("Part one:", result)

time = int("".join([str(t) for t in times]))
distance = int("".join([str(d) for d in distances]))
print("Part two:", beat(time, distance))