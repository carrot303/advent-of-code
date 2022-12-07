from read_input import get_input_data


input_data = get_input_data(day=6)


COUNT_DISTINCT_CHARS_PUZZLE_ONE = 4
COUNT_DISTINCT_CHARS_PUZZLE_TWO = 14

def solve_puzzle_one() -> int:
    for index, char in enumerate(input_data):
        four_chars = input_data[index:index+COUNT_DISTINCT_CHARS_PUZZLE_ONE]
        different_chars = set(four_chars)
        if len(different_chars) == COUNT_DISTINCT_CHARS_PUZZLE_ONE:
            return index + COUNT_DISTINCT_CHARS_PUZZLE_ONE


def solve_puzzle_two() -> int:
    for index, char in enumerate(input_data):
        four_chars = input_data[index:index+COUNT_DISTINCT_CHARS_PUZZLE_TWO]
        different_chars = set(four_chars)
        if len(different_chars) == COUNT_DISTINCT_CHARS_PUZZLE_TWO:
            return index + COUNT_DISTINCT_CHARS_PUZZLE_TWO


if __name__ == '__main__':
    print(f"Result of puzzle one: {solve_puzzle_one()}")
    print(f"Result of puzzle two: {solve_puzzle_two()}")