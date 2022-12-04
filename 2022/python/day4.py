from read_input import get_input_data

input_data = get_input_data(day=4)


def solve_puzzle_one() -> int:
    sections = input_data.splitlines() # --> ['2-4,4-8', '4-5,5-7', ...]
    count = 0
    for secion in sections:
        first_pair, second_pair = secion.split(',') # --> ['2-4', '4-8']

        # Following code result --> [2, 4]
        first_pair_id_start, first_pair_id_stop = [
            int(num) for num in first_pair.split('-')
        ]
        # Extract set number --> {2,3,4}
        first_pair_range = set(range(first_pair_id_start, first_pair_id_stop+1))

        # Following code result --> [4, 8]
        second_pair_start, second_pair_stop = [
            int(num) for num in second_pair.split('-')
        ]
        # Extract set number --> {4,5,6,7,8}
        second_pair_range = set(range(second_pair_start, second_pair_stop+1))
        
        # is fully contain?
        if second_pair_range > first_pair_range:
            fully_contain_set = first_pair_range.difference(second_pair_range)
        else:
            fully_contain_set = second_pair_range.difference(first_pair_range)

        if len(fully_contain_set) == 0:
            # it's a fully contain
            count += 1
    return count


def solve_puzzle_two() -> int:
    sections = input_data.splitlines() # --> ['2-4,4-8', '4-5,5-7', ...]
    count = 0
    for secion in sections:
        first_pair, second_pair = secion.split(',') # --> ['2-4', '4-8']

        # Following code result --> [2, 4]
        first_pair_id_start, first_pair_id_stop = [
            int(num) for num in first_pair.split('-')
        ]
        # Extract set number --> {2,3,4}
        first_pair_range = set(range(first_pair_id_start, first_pair_id_stop+1))

        # Following code result --> [4, 8]
        second_pair_start, second_pair_stop = [
            int(num) for num in second_pair.split('-')
        ]
        # Extract set number --> {4,5,6,7,8}
        second_pair_range = set(range(second_pair_start, second_pair_stop+1))
        
        # has intersection items?
        fully_contain_set = second_pair_range.intersection(first_pair_range)
        if len(fully_contain_set) != 0:
            # has some equal section id
            count += 1
    return count


if __name__ == '__main__':
    print(f'Answer part one: {solve_puzzle_one()}')
    print(f'Answer part two: {solve_puzzle_two()}')