class Trees:
    def __init__(self, heights: list[list[int]]) -> None:
        self.heights = heights
        self.rows = len(heights)
        self.columns = len(heights[0])
        self.visibility = [[0] * len(row) for row in self.heights]
        self.visible_trees = 0

    def calc_visibility(self):
        # from left to right:
        for i in range(self.rows):
            self.visibility[i][0] = 1
            curr_max = self.heights[i][0]
            for j in range(self.columns):
                if self.heights[i][j] > curr_max:
                    self.visibility[i][j] = 1
                    curr_max = self.heights[i][j]

        for line in self.visibility:
            print(line) 

        print()

        for j in range(self.columns):
            self.visibility[0][j] = 1
            curr_max = self.heights[0][j]
            for i in range(self.rows):
                if self.heights[i][j] > curr_max:
                    self.visibility[i][j] = 1
                    curr_max = self.heights[i][j]

        for line in self.visibility:
            print(line) 


        # хранить/заполнять матрицу минимумов, чтобы продвигаться как бы сразу слева направо и сверху вниз а потом наоборот



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

    # assert trees.visible_trees == 21

    expected_visibility = [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 0, 1],
        [1, 1, 0, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1]
    ]
    assert trees.visibility == expected_visibility

        
