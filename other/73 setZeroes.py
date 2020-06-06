from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        row_zero = set()
        col_zero = set()
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    row_zero.add(i)
                    col_zero.add(j)
        for i in range(row):
            for j in range(col):
                if i in row_zero or j in col_zero:
                    matrix[i][j] = 0


if __name__ == '__main__':
    a = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    b = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ]
    sol = Solution()
    sol.setZeroes(a)
    sol.setZeroes(b)
    print(a)
    print(b)
