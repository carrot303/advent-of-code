from read_input import get_input_data



input_data = get_input_data(14)
rock_paths = input_data.splitlines()

ROCK_COORDS = set()

for rock_path in rock_paths:
    paths = rock_path.split('->')
    for i in range(len(paths)-1):
        current_x, current_y = [int(c) for c in paths[i].strip().split(',')]
        next_path = paths[i+1].strip()
        next_x, next_y = [int(c) for c in next_path.split(',')]

        if next_x == current_x:
            range_ = range(current_y, next_y+1) if current_y < next_y else range(next_y, current_y+1)  
            coordinates = zip([next_x]*len(range_), range_)
            [ROCK_COORDS.add(coord) for coord in coordinates]
        elif current_y == next_y:
            range_ = range(current_x, next_x+1) if current_x < next_x else range(next_x, current_x+1)
            coordinates = zip(range_, [next_y]*len(range_))
            [ROCK_COORDS.add(coord) for coord in coordinates]

SANDS_COORDS = []


def fall_sand_until_rest(start_x: int = 500, start_y: int = 0, part: int = None):
    max_y = max(*ROCK_COORDS, key=lambda x: x[1])[1]
    stand_y = max_y
    if part == 2:
        stand_y = max_y+1
    x, y = start_x, start_y
    while True:
        if y == stand_y:
            SANDS_COORDS.append((x, y))
            return False # falling into the endless
        if (x, y+1) not in [*SANDS_COORDS, *ROCK_COORDS]:
            y += 1
            continue
        if (x-1, y+1) not in [*SANDS_COORDS, *ROCK_COORDS]:
            x -= 1
            y += 1
            continue
        if (x+1, y+1) not in [*SANDS_COORDS, *ROCK_COORDS]:
            x += 1 
            y += 1
            continue
        SANDS_COORDS.append((x, y))
        if (x, y) == (500, 0):
            return None
        return True


def solve_part_one():
    SANDS_COORDS.clear()
    sand_counts = 0 
    while True:
        res = fall_sand_until_rest()
        if res is False:
            break
        sand_counts += 1 
    return sand_counts


def solve_part_two():
    SANDS_COORDS.clear()
    sand_units = 0
    while True:
        res = fall_sand_until_rest(part=2)
        sand_units += 1
        if res == None:
            break
    return sand_units


if __name__ == '__main__':
    print('Result for part one:', solve_part_one())
    print('Result for part two:', solve_part_two())