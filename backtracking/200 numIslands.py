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
        print(visited)
        self.numIslands_memo()
        return res[0]

    def numIslands_memo(self):
        # 结束条件是什么
        for i in range(m):
            for j in range(n):
                if visited[i][j]:
                    pass
                else:
                    self.numIslands_memo()


if __name__ == '__main__':
    nums = [
        ['1', '1', '0', '0', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1']
    ]
    sol = Solution()
    print(sol.numIslands(grid=nums))
