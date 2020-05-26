from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List:
        n = len(matrix)
        m = len(matrix[0])
        res = []
        for i in range(n):
            for j in range(m):
                res.append(self.isMatrix(matrix, i, j))
        return res

    def isMatrix(self, matrix, i, j):
        pass


if __name__ == '__main__':
    sol = Solution()
    a = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(sol.spiralOrder(a))
