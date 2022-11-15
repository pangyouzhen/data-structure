from typing import List

# TODO
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # 遍历过为True，未遍历未False
        grid_flag = [[False] * n for i in range(m)]
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        res = 0

        def dfs(grid, i, j, area):
            if 0 <= i < m and 0 <= j < n:
                if grid[i][j] == 1 and grid_flag[i][j] is False:
                    grid_flag[i][j] = True
                    area += 1
                    for k, v in directions:
                        dfs(grid, i + k, j + v, area)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and grid_flag[i][j] is False:
                    area = 1
                    dfs(grid, i, j, area)
                    if area > res:
                        res = area
        return res


if __name__ == '__main__':
    islands = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
               [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
               [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    func = Solution().maxAreaOfIsland
    print(func(islands))
