from collections import defaultdict

with open("inputs/day5.txt") as file:
	puzzle = file.read().strip()



first, *maps = puzzle.split("\n\n")
# Part one
seeds = list(map(int, first.split()[1:]))

# Part two
seed_starts = list(map(int,first.split()[1::2]))
seed_length = list(map(int,first.split()[2::2]))

corresponds = defaultdict(list)


def get_correspond(std, number):
	maps = corresponds[std]
	for m in maps:
		dest, source, length = m
		if number >= source and ((number-source)+dest) < dest+length:
			return (number-source)+dest
	return number


for m in maps:
	a = m.split("\n")
	source_to_dest = a[0].split()[0]
	for i in range(1, len(a)):
		corresponds[source_to_dest].append(list(map(int,a[i].split())))


# Part one
lowest_location = 1e10
for seed in seeds:
	soil = get_correspond("seed-to-soil", seed)
	fertilizer = get_correspond("soil-to-fertilizer", soil)
	water = get_correspond("fertilizer-to-water", fertilizer)
	light = get_correspond("water-to-light", water)
	temperature = get_correspond("light-to-temperature", light)
	humidity = get_correspond("temperature-to-humidity", temperature)
	location = get_correspond("humidity-to-location", humidity)
	lowest_location = location if location < lowest_location else lowest_location

print(lowest_location)


# Part two
lowest_location = 1e10
for r in range(len(seed_starts)):
	for seed in range(seed_starts[r],seed_starts[r]+seed_length[r]):
		soil = get_correspond("seed-to-soil", seed)
		fertilizer = get_correspond("soil-to-fertilizer", soil)
		water = get_correspond("fertilizer-to-water", fertilizer)
		light = get_correspond("water-to-light", water)
		temperature = get_correspond("light-to-temperature", light)
		humidity = get_correspond("temperature-to-humidity", temperature)
		location = get_correspond("humidity-to-location", humidity)
		lowest_location = location if location < lowest_location else lowest_location

print(lowest_location)