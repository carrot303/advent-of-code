from enum import Enum, auto
from typing import Optional

from read_input import get_input_data

input_data = get_input_data(day=2)

class Move(Enum):
    ROCK = auto()
    PAPER = auto()
    SCISSORS = auto()


class Action(Enum):
    WIN = auto()
    LOSE = auto()
    DRAW = auto()


def dispatch(*, your_choose: Move, opponent_choose: Move) -> Optional[Action]:
    """Returns:
        - True: move_one win
        - False: move_two win
        - None: draw
    """
    match (your_choose, opponent_choose):
        case (Move.ROCK, Move.ROCK) | (Move.PAPER, Move.PAPER) | (Move.SCISSORS, Move.SCISSORS):
            # it's draw
            return Action.DRAW
        case (Move.ROCK, Move.SCISSORS) | (Move.SCISSORS, Move.PAPER) | (Move.PAPER, Move.ROCK):
            # Move one is won
            return Action.WIN
        case (Move.SCISSORS, Move.ROCK) | (Move.PAPER, Move.SCISSORS) | (Move.ROCK, Move.PAPER):
            # Move two is won
            return Action.LOSE


MOVES = {
    'A': Move.ROCK,
    'B': Move.PAPER,
    'C': Move.SCISSORS,
    'X': Move.ROCK,
    'Y': Move.PAPER,
    'Z': Move.SCISSORS
}

POINT_PER_MOVE = {
    Move.ROCK: 1,
    Move.PAPER: 2,
    Move.SCISSORS: 3,
}


POINTS_PER_ACTION = {
    Action.WIN: 6,
    Action.LOSE: 0,
    Action.DRAW: 3,
}


MOVES_MEANS = {
    'Y': Action.DRAW,
    'X': Action.LOSE,
    'Z': Action.WIN,
}


WIN_MOVE_VS_MOVE = {
    Move.ROCK: Move.PAPER, # rock defeat paper
    Move.SCISSORS: Move.ROCK, # scissors defeat rock
    Move.PAPER: Move.SCISSORS, # paper defeat scissors
}

LOSE_MOVE_VS_MOVE = {
    Move.PAPER: Move.ROCK, # rock defeat paper
    Move.ROCK: Move.SCISSORS, # scissors defeat rock
    Move.SCISSORS: Move.PAPER, # paper defeat scissors
}


def solve_puzzle_one():
    # Split each move into a list of moves -> ['A X', 'B Z', ..., 'C Y']
    moves = input_data.strip().splitlines()
    your_points = 0
    for move in moves:
        # ['A', 'X'] -> [Move.Rock, Move.Paper]
        opponent_choose, your_choose = [MOVES[choose] for choose in move.split()]
        your_points += POINTS_PER_ACTION[dispatch(your_choose=your_choose, opponent_choose=opponent_choose)] + POINT_PER_MOVE[your_choose]
    return your_points


def solve_puzzle_two():
    # Split each move into a list of moves -> ['A X', 'B Z', ..., 'C Y']
    moves = input_data.strip().splitlines()
    points = 0
    for move in moves:
        # ['A', 'X'] -> [Move.Rock, Move.Paper]
        opponent_choose, your_choose = [MOVES[choose] for choose in move.split()]
        action = MOVES_MEANS[move.split()[1]]
        if action == Action.DRAW:
            your_choose = opponent_choose
        elif action == Action.WIN:
            your_choose = WIN_MOVE_VS_MOVE[opponent_choose]
        elif action == Action.LOSE:
            your_choose = LOSE_MOVE_VS_MOVE[opponent_choose]
        points += POINTS_PER_ACTION[action] + POINT_PER_MOVE[your_choose]
    return points


if __name__ == '__main__':
    print('Puzzle two part 1:', solve_puzzle_one()) # most : 10816
    print('Puzzle two part 2:', solve_puzzle_two()) # most : 11652