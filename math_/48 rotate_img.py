from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()

        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


# (0,0)  reverse (2,0) -> (0,2)
# (0,1)  reverse (2,1) -> (1,2)
# (0,2)  reverse (2,2) -> (2,2)
# (1,0)  reverse (0,1) -> (0,1)
# (1,1)  reverse (1,1) -> (1,1)
# (1,2)  reverse (2,1) -> (2,1)
# (2,0)  reverse (0,0) -> (0,0)
# (2,1)  reverse (0,1) -> (1,0)
# (2,2)  reverse (0,2) -> (2,0)

if __name__ == '__main__':
    sol = Solution()
    a = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    sol.rotate(a)
    print(a)
