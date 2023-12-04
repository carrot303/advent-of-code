
with open("inputs/day2.txt") as file:
    puzzle = file.read().strip()

result = 0
for line in puzzle.strip().split('\n'):
    id_, rest = line.split(":")
    sets = rest.split(";")
    for s in sets:
        game_cubes = {"red": 0, "blue": 0, "green": 0}
        configs = s.split(",")
        for config in configs:
            n, cube = config.strip().split()
            game_cubes[cube] = int(n)
        if game_cubes["red"] > 12 or game_cubes["green"] > 13 or game_cubes["blue"] > 14:
            break
    else:
        result += int(id_.split()[1])

print(result)

result = 0
for line in puzzle.strip().split('\n'):
    id_, rest = line.split(":")
    sets = rest.split(";")
    game_cubes = {"red": [], "blue": [], "green": []}
    for s in sets:
        for config in s.split(","):
            n, cube = config.strip().split()
            game_cubes[cube].append(int(n))

    r, g, b = max(game_cubes["red"]), max(game_cubes["green"]), max(game_cubes["blue"])
    result += r*g*b


print(result)
