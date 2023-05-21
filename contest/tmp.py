from typing import *
from pprint import pprint

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.r = len(grid)
        self.c = len(grid[0])
        self.ans = 0
        for i in range(self.r):
            for j in range(self.c):
                if grid[i][j] == 1:
                    area = self.dfs(grid, i, j)
                    self.ans = max(area, self.ans)
        return self.ans

    def dfs(self, grid, i, j):
        if 0 <= i < self.r and 0 <= j < self.c and grid[i][j] == 1:
            grid[i][j] = 2
            area = 1
            area += self.dfs(grid,i - 1, j)
            area += self.dfs(grid,i + 1, j)
            area += self.dfs(grid,i, j - 1)
            area += self.dfs(grid,i, j + 1)
            return area
        else:
            return 0

if __name__ == "__main__":
    func = Solution().maxAreaOfIsland
    grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
    print(func(grid))
