from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        res = 0

        def dfs(grid, i, j, area):
            if not(0 <= i < m and 0 <= j < n and grid[i][j] == 1):
                return 0
            grid[i][j] = 2
            area = 1
            for k, v in directions:
                area += dfs(grid, i + k, j + v, area)
            return area
                
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    # 这里最关键的是传入的 area 如何传出来, 肯定是return， 但是怎么return是问题
                    area = 1
                    area = dfs(grid, i, j, area)
                    if area > res:
                        res = area
                area = 0
        return res


if __name__ == '__main__':
    islands = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
               [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
               [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    func = Solution().maxAreaOfIsland
    print(func(islands))
