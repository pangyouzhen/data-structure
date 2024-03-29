from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row_matrix = self.matrix[row1:row2 + 1]
        return sum(sum(i[col1:col2 + 1]) for i in row_matrix)


if __name__ == '__main__':
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ]
    nums = NumMatrix(matrix)
    print(nums.sumRegion(2, 1, 4, 3))
