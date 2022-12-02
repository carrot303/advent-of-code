import day1
import day2


# Test puzzle day one
def test_answer_day_one_part_one():
    assert day1.solve_puzzle_one() == 64929


def test_answer_day_one_part_two():
    assert day1.solve_puzzle_two() == 193697


# Test puzzle day one
def test_answer_day_two_part_one():
    assert day2.solve_puzzle_one() == 10816


def test_answer_day_two_part_two():
    assert day2.solve_puzzle_two() == 11657
