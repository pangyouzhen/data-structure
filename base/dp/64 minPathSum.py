from typing import List
from pprint import pprint


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * n for _ in range(m)]
        # 第一行
        rows_val = 0
        for ind, val in enumerate(range(n)):
            rows_val += grid[0][ind]
            dp[0][ind] = rows_val
        # 第一列
        col_val = 0
        for ind, val in enumerate(range(m)):
            col_val += grid[ind][0]
            dp[ind][0] = col_val
        # 其余的数字
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[-1][-1]


# dp = [
# [1, 4, 5],
# [2, 7, 6],
# [6, 8, 7]]

if __name__ == '__main__':
    ls = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]

    sol = Solution()
    print(sol.minPathSum(ls))
