import re

from read_input import get_input_data

input_data = get_input_data(day=5)


REGEX_EXTRACT_CRATES = re.compile(r'(\[[A-Z]\]|\s{3})\s?')


def _prepare_stack(stack_crates: list[str], stack_numbers: list[str]) -> dict[str, list]:
    """Preparing the stack
    
    This is just collect each crate for their stack
    and put them into the stacks

    for example consider following stacks of crates:    
        ```
        >>> stack_input = '''
            [D]    
        [N] [C]    
        [Z] [M] [P]
        1   2   3
        '''
        >>> stack_number = ['1', '2', '3']
        >>> _prepare_stack(stack_input, stack_number)
        {
            '1': ['Z', 'N'],
            '2': ['M', 'C', 'D'],
            '3': ['P']
        }
        ```
    """
    crates_per_stack = {stack_number: [] for stack_number in stack_numbers}
    for crate_in_row in stack_crates: # crate_in_row --> '[N] [D]     [F]'
        row_crates: list[str] = REGEX_EXTRACT_CRATES.findall(crate_in_row) # --> ['[N]', '[D]', '   ', '[F]']
        crates_per_id = dict(zip(stack_numbers, row_crates)) # --> {'1': '[N]', '2': '[D]', '3': '   ', '4': '[F]'}
        for _id, crate in crates_per_id.items():
            if crate.strip(): # non '   '
                crates_per_stack[_id].insert(0, crate[1]) # --> insert 'N' to first of stack
    return crates_per_stack


def solve_puzzle_one() -> str:
    stack_crates_str, steps_str = input_data.split('\n\n')

    steps = steps_str.splitlines() # ['move 1 from 2 to 1', ...]
    *stack_crates, stack_numbers = stack_crates_str.splitlines()
    stack_numbers = stack_numbers.split()
    
    crates_per_stack = _prepare_stack(stack_crates, stack_numbers)

    # Execute steps for stacks
    for step in steps:
        count, crates_from_id, crates_to_id = re.findall(r'\d+', step)
        for _ in range(int(count)):
            # Pop from `crates_from_id` stack and push to `crates_to_id` stack
            crate_from = crates_per_stack[crates_from_id].pop()
            crates_per_stack[crates_to_id].append(crate_from)
    
    return "".join([s.pop() for s in crates_per_stack.values()])


def solve_puzzle_two() -> str:
    stack_crates_str, steps_str = input_data.split('\n\n')

    steps = steps_str.splitlines() # ['move 1 from 2 to 1', ...]
    *stack_crates, stack_numbers = stack_crates_str.splitlines()
    stack_numbers = stack_numbers.split()
    
    
    crates_per_stack = _prepare_stack(stack_crates, stack_numbers)

    # Execute steps for stacks
    for step in steps:
        count, crates_from_id, crates_to_id = re.findall(r'\d+', step)
        temp_crates = []
        for _ in range(int(count)):
            # Pop from `crates_from_id` stack and push to `crates_to_id` stack
            crate_from = crates_per_stack[crates_from_id].pop()
            temp_crates.insert(0, crate_from)
        
        crates_per_stack[crates_to_id].extend(temp_crates)
        
    return "".join([s.pop() for s in crates_per_stack.values()])


if __name__ == '__main__':
    print(f"Result puzzle one: {solve_puzzle_one()}")
    print(f"Result puzzle two: {solve_puzzle_two()}")