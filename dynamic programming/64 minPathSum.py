from typing import List


class Solution:
    #  不使用递归，直接使用动态规划
    def minPathSum2(self, grid: List[List[int]]) -> int:
        return self.uniquePath(0, 0, grid)

    def uniquePath(self, param, param1, grid):
        if param < 0 or param1 < 0:
            return 0
        else:
            return min(self.uniquePath(param - 1, param1, grid) + grid[param][param1],
                       self.uniquePath(param, param1 - 1, grid) + grid[param][param1])

    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp = [[0] * cols for _ in range(rows)]
        dp[0][0] = grid[0][0]
        for row in range(rows):
            for col in range(cols):
                if row == 0 and col == 0:
                    continue
                elif row == 0:
                    dp[row][col] = dp[row][col - 1] + grid[row][col]
                elif col == 0:
                    dp[row][col] = dp[row - 1][col] + grid[row][col]
                else:
                    dp[row][col] = min(dp[row - 1][col], dp[row][col - 1]) + grid[row][col]
        return dp[rows - 1][cols - 1]


# f(i,j) = min(f(x-1,j)+k,f(j-1,i)+k)
if __name__ == '__main__':
    ls = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    sol = Solution()
    print(sol.minPathSum(ls))
