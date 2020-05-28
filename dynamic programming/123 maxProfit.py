from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i):
                pass
        # dp[i][j] =
        return dp[n - 1][n - 1]


if __name__ == '__main__':
    sol = Solution()
    sol.maxProfit([1, 2, 3, 4, 5])
    print(sol.maxProfit([0, 3, 5, 0, 0, 3, 1, 4, 1, 5]))
