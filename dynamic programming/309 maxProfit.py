from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hesitate = 0
        m = len(prices)
        dp = [[0] * (m + 1) for _ in range(m + 1)]
        for i in range(1, m):
            for j in range(i):
                if hesitate % 3 == 0:
                    pass
                elif hesitate % 3 == 1:
                    dp[i][j] = (prices[i] - prices[i - 1]) + dp[i - 1][j - 1]
            hesitate += 1
        print(dp)
        return dp[m][m]


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3, 0, 2]
    print(sol.maxProfit(nums))
