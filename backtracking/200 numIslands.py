from typing import List


# 回溯法+方向判断
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # 遍历过为True，未遍历未False
        grid_flag = [[False] * n for i in range(m)]
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        res = 0

        def dfs(grid, i, j):
            if 0 <= i < m and 0 <= j < n:
                if grid[i][j] == "1" and grid_flag[i][j] is False:
                    grid_flag[i][j] = True
                    for k, v in directions:
                        dfs(grid, i + k, j + v)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and grid_flag[i][j] is False:
                    res += 1
                    dfs(grid, i, j)

        return res


class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 遍历过为True，未遍历未False
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res += self.dfs(grid,i,j)
        return res

    def dfs(self, grid, i, j):
        if self.not_in_grid(grid, i, j):
            return 0
        if grid[i][j] != "1":
            return 0
        grid[i][j] = 2
        return 1 + self.dfs(grid, i - 1, j) + self.dfs(grid, i + 1, j) + self.dfs(grid, i, j - 1) + self.dfs(grid, i, j + 1)

    def not_in_grid(self, grid, i, j):
        return i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0])


if __name__ == "__main__":
    nums = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    sol = Solution2()
    print(sol.numIslands(grid=nums))
