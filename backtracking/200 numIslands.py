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


if __name__ == '__main__':
    nums = [
        ['1', '1', '0', '0', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1']
    ]
    sol = Solution()
    print(sol.numIslands(grid=nums))
