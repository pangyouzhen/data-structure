from typing import List


# 回溯法+方向判断
class Solution:
    # 联通图的个数-染色问题
    def numIslands(self, grid: List[List[str]]) -> int:
        n_rows = len(grid)
        if n_rows == 0:
            return 0
        n_columns = len(grid[0])
        nums_islands = 0
        for i in range(n_rows):
            for j in range(n_columns):
                if grid[i][j] == "1":
                    nums_islands += 1
                    self.dfs(grid, i, j)
        return nums_islands

    def dfs(self, grid, i, j):
        print(i,j)
        # 这里是关键，如果遍历过了就重置为0，这里没有终止条件？
        grid[i][j] = 0
        nr, nc = len(grid), len(grid[0])
        for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                self.dfs(grid, x, y)


if __name__ == '__main__':
    nums = [
        ['1', '1', '0', '0', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1']
    ]
    sol = Solution()
    print(sol.numIslands(grid=nums))
