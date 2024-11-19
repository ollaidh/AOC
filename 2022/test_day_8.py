class Trees:
    def __init__(self, heights: list[list[int]]) -> None:
        self.heights = heights
        self.visibility = [[0] * len(row) for row in self.heights]
        self.visible_trees = 0

    def calc_visibility(self):
        pass


def test_calc_visibility():
    trees_matrix = [
        [3, 0, 3, 7, 3],
        [2, 5, 5, 1, 2],
        [6, 5, 3, 3, 2],
        [3, 3, 5, 4, 9],
        [3, 5, 3, 9, 0]
    ]

    trees = Trees(trees_matrix)
    trees.calc_visibility()
    assert trees.visible_trees == 21

    expected_visibility = [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 0, 1],
        [1, 1, 0, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1]
    ]
    assert trees.visibility == expected_visibility

        
