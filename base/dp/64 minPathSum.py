from typing import List
from pprint import pprint


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        # 关键是前面这两个的判定, 这是针对第一行和第一列进行判定的
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        pprint(dp)
        # dp = [
        # [1, 4, 5],
        # [2, 0, 0],
        # [6, 0, 0]]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        pprint(dp)
        return dp[m - 1][n - 1]
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
