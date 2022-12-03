import string

from read_input import get_input_data


input_data = get_input_data(day=3)


class Rucksack:
    def __init__(self, rucksack: str) -> None:
        self.rucksack = rucksack
        self.length_runcksack = len(rucksack)
        self.length_per_compartment = self.length_runcksack // 2
        
        self.first_compartment = ""
        self.second_compartment = ""
    
    def split_compartments(self) -> None:
        """Split rucksack into two half of compartments"""
        self.first_compartment = self.rucksack[:self.length_per_compartment]
        self.second_compartment = self.rucksack[self.length_per_compartment:]
    
    def get_common_character(self) -> str:
        """Return the only common chracter in two compartments"""
        common_chars = set(self.first_compartment).intersection(self.second_compartment)
        return list(common_chars)[0]
    
    @staticmethod
    def get_point(char: str) -> int:
        """Get point of given character"""
        return string.ascii_letters.index(char) + 1
    
    @staticmethod
    def get_common_char_in_rucksacks(*rucksacks: list[str]) -> str:
        """Get common char in given rucksacks"""
        first_rucksack, *rest = rucksacks
        common_chars = set(first_rucksack).intersection(*rest)
        return list(common_chars)[0]


def solve_puzzle_one() -> int:
    """Solve part one in day 3"""
    rucksacks = input_data.splitlines()
    result = 0
    for rucksack in rucksacks:
        r = Rucksack(rucksack)
        r.split_compartments()
        common_char = r.get_common_character()
        result += Rucksack.get_point(common_char)
    return result


def solve_puzzle_two() -> int:
    """Solve part two in day 3"""
    rucksacks = input_data.splitlines()
    result = 0
    for index, r in enumerate(rucksacks):
        if index % 3 == 0:
            common_char = Rucksack.get_common_char_in_rucksacks(*rucksacks[index:index+3])
            result += Rucksack.get_point(common_char)
    return result


if __name__ == '__main__':
    print(f'Answer of part one: {solve_puzzle_one()}')
    print(f'Answer of part two: {solve_puzzle_two()}')