from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        t = [j for i in grid for j in i]
        if 1 not in t:
            return 0
        directions = [
            [0, 1],
            [0, -1],
            [-1, 0],
            [1, 0]
        ]
        row = len(grid)
        col = len(grid[0])
        if row == 1 and col == 1 and grid[0][0] != 1:
            return 0

        queue = []
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append((i, j))

        time = -1
        while queue:
            current_len = len(queue)
            for _ in range(current_len):
                i, j = queue.pop(0)
                for x, y in directions:
                    temp_i = i + x
                    temp_j = j + y
                    if 0 <= temp_i < row and 0 <= temp_j < col and grid[temp_i][temp_j] == 1:
                        grid[temp_i][temp_j] = 2
                        queue.append((temp_i, temp_j))
            time += 1
        for eachrow in grid:
            if 1 in eachrow:
                return -1
        return time


if __name__ == '__main__':
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    sol = Solution()
    print(sol.orangesRotting(grid))
