from typing import List
from Cyberbrain import trace


class Solution:
    @trace
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] < 0:
                    res += 1
        return res
