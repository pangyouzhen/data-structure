from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        global m
        m = len(grid)
        global n
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                return self.dfs(grid, i, j)

    def dfs(self, grid, i, j):
        if 0 <= i < m and 0 <= j < n:
            directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            for h, v in directions:
                self.dfs(grid, i + h, j + v)
