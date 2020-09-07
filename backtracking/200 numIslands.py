from typing import List


class Solution:
    def __init__(self):
        self.directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    def numIslands(self, grid: List[List[str]]) -> int:
        global visited, m, n, res
        m = len(grid)
        n = len(grid[0])
        res = [0]
        visited = [[False] * n for _ in range(m)]
        self.numIslands_memo()
        return res[0]

    def numIslands_memo(self):
        pass
