from typing import List


# 回溯法+方向判断
# todo
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        t = 0
        grid_bool = [[False] * len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid_bool[i][j] is False:
                    if grid[i][j] == 1:
                        grid_bool[i][j] = True
                        t += 1
                        for m in directions:
                            pass
        return t


if __name__ == '__main__':
    nums = [
        ['1', '1', '0', '0', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1']
    ]
    sol = Solution()
    print(sol.numIslands(grid=nums))
