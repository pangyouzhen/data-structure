from typing import List


class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        a = set(list(range(1, n + 1)))
        for i in matrix:
            if set(i) != a:
                return False
        for i in range(n):
            cols = []
            for j in matrix:
                cols.append(j[i])
            if set(cols) != a:
                return False
        return True


if __name__ == "__main__":
    func = Solution().checkValid
    matrix = [[1, 2, 3], [3, 1, 2], [2, 3, 1]]
    print(func(matrix))
