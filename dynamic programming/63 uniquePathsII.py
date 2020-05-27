from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        cur = 1
        for i in range(n):
            if obstacleGrid[0][i] == 1:
                cur = 0
            dp[0][i] = cur
        cur =1
        for j in range(m):
            if obstacleGrid[j][0] == 1:
                cur = 0
            dp[j][0] = cur
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
if __name__ == "__main__":
    sol = Solution()
    obs = [[0,0,0],[0,1,0],[0,0,0]]
    print(sol.uniquePathsWithObstacles(obs))
