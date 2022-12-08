from read_input import get_input_data


input_data = get_input_data(day=8)


class Jungle:
    def __init__(self) -> None:
        # Making the matrix of trees
        self.trees = [
            [int(col) for col in row]
            for row in input_data.strip().splitlines()
        ]

        # Making the interior of trees
        self.interior_trees = [
            [tree for tree in row[1:len(row)-1]]
            for row in self.trees[1:len(self.trees)-1]
        ]

        self.trees_count = sum([len(row) for row in self.trees])
        self.interior_trees_count = sum([len(row) for row in self.interior_trees])
        self.visible_count = self.trees_count - self.interior_trees_count
        self.possible_view_tree: list[int] = []

    def find_visible_trees(self) -> None:
        for index_row, row in enumerate(self.interior_trees, start=1):
            for index_col, tree in enumerate(row, start=1):
                if self.is_visible(index_row, index_col, tree):
                    self.visible_count += 1
    
    def calculate_highest_count_of_trees(self):
        for index_row, row in enumerate(self.interior_trees, start=1):
            for index_col, tree in enumerate(row, start=1):
                self.possible_view_tree.append(self.get_visible_trees_of_tree(index_row, index_col, tree))
        return max(self.possible_view_tree)
    
    def is_visible(self, index_row: int, index_col: int, tree: int) -> bool:
        """Check visiblity of given tree in specfic position"""
        right_trees, left_trees, top_trees, bottom_trees = self.get_among_trees(index_row, index_col)
        # Is visble if the tree is lower than tallest tree in other direction among given trees
        is_visible = any(
            [
                tree > other_tree for other_tree in 
                [max(right_trees), max(left_trees), max(top_trees), max(bottom_trees)]
            ]
        )
        return is_visible

    def get_among_trees(self, index_row: int, index_col: int) -> tuple[list]:
        """Returns the among trees of given tree"""
        right_trees = self.trees[index_row][index_col+1:]
        left_trees = self.trees[index_row][:index_col]
        bottom_trees = []
        top_trees = []
        
        for i_row, row in enumerate(self.trees[index_row+1:]):
            for i_col, col in enumerate(row):
                if index_col == i_col:
                    bottom_trees.append(col)

        for i_row, row in enumerate(self.trees[:index_row]):
            for i_col, col in enumerate(row):
                if index_col == i_col:
                    top_trees.append(col)
        
        return right_trees, left_trees, top_trees, bottom_trees

    def get_visible_trees_of_tree(self, index_row: int, index_col: int, tree: int) -> int:
        """Return trees that is visible from given tree
        if we look at direction of that tree"""
        right_trees, left_trees, top_trees, bottom_trees = self.get_among_trees(index_row, index_col)
        c = 1
        c *= self.get_count_visible_tree_of_spec_direction(tree, right_trees)
        c *= self.get_count_visible_tree_of_spec_direction(tree, reversed(left_trees))
        c *= self.get_count_visible_tree_of_spec_direction(tree, reversed(top_trees))
        c *= self.get_count_visible_tree_of_spec_direction(tree, bottom_trees)
        return c
    
    def get_count_visible_tree_of_spec_direction(self, current_tree: int, trees: list[int]) -> int:
        """Returns the count of visible trees
        when view from given tree toward specific direction"""
        c = 0
        for tree in trees:
            c += 1
            if tree >= current_tree:
                break
        return c


def solve_puzzle_one() -> int:
    jungle = Jungle()
    jungle.find_visible_trees()
    return jungle.visible_count


def solve_puzzle_two() -> int:
    jungle = Jungle()
    return jungle.calculate_highest_count_of_trees()


if __name__ == '__main__':
    print(f'Result for puzzle one: {solve_puzzle_one()}')
    print(f'Result for puzzle two: {solve_puzzle_two()}')