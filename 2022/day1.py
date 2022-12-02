# Puzzle one

from read_input import get_input_data

_input = get_input_data(day=1)


def solve_puzzle_one():
    # Get sum of all callories per elf
    elves_cariies_sum = [
        sum([int(f) for f in elf_carry.splitlines()])
        for elf_carry in _input.split('\n\n')
    ]
    result = max(elves_cariies_sum)
    return result


def solve_puzzle_two():
    # Get sum of all callories per elf
    elves_cariies_sum = [
        sum([int(f) for f in elf_carry.splitlines()])
        for elf_carry in _input.split('\n\n')
    ]
    first_elf, second_elf, third_elf, *rest = sorted(elves_cariies_sum, reverse=True)
    result = sum([first_elf, second_elf, third_elf])
    return result


if __name__ == '__main__':
    print('Puzzle one part 1:', solve_puzzle_one()) # most : 64929
    print('Puzzle one part 2:', solve_puzzle_two()) # most : 193697