from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = []
        m = len(mat)
        for i in range(m):
            if m - i - 1 == i:
                res.append(mat[i][i])
            else:
                res.append(mat[i][i])
                res.append(mat[m - i - 1][i])
        return sum(res)


if __name__ == '__main__':
    mat = [[5]]
    sol = Solution()
    print(sol.diagonalSum(mat))
