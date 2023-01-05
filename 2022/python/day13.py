from read_input import get_input_data


input_data = get_input_data(day=13)


def solve_puzzle_one() -> int:
    pairs = input_data.split('\n\n')

    sum_ = 0
    for pair_id in range(1, len(pairs)+1):
        left, right = [eval(p) for p in pairs[pair_id-1].splitlines()]
        status = compare(left, right)
        if status == 1:
            sum_ += pair_id
    return sum_


def compare(left: list | int, right: list | int) -> int:
    '''
    returns:
        1: Order
        0: Not Order
        -1: Equal but left side ran
    '''
    if isinstance(left, list) and isinstance(right, list):
        ran = False
        try:
            zipped = list(zip(left, right, strict=True))
        except ValueError:
            zipped = list(zip(left, right))
            ran = True

        for lf, rt in zipped:
            res = compare(lf, rt)
            if res is not None:    
                return res

        if ran:
            return 1 if len(left) < len(right) else -1

    if isinstance(left, int) and isinstance(right, list):
        return compare([left], right)
    if isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])
    
    if isinstance(left, int) and isinstance(right, int):
        if int(left) > int(right):
            return 0
        elif int(left) < int(right):
            return 1


if __name__ == '__main__':
    print('Part One: ', solve_puzzle_one())
    