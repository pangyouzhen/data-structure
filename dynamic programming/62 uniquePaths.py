from functools import lru_cache


class Solution:
    @lru_cache()
    def uniquePaths2(self, m, n):
        if m <= 0 or n <= 0:
            return 0
        if m == 1 and n == 1:
            return 1
        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)

    def uniquePaths(self, m, n):
        dp = [[0] * m for _ in range(n)]
        dp[0][0] = 1
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    dp[i][j] = dp[i][j - 1]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        # print(dp)
        return dp[n - 1][m - 1]


if __name__ == '__main__':
    sol = Solution()
    assert sol.uniquePaths(3, 2) == 3
    assert sol.uniquePaths(7, 3) == 28
    # print(sol.uniquePaths(3, 2))
