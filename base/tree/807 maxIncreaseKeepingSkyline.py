from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        l = len(grid)
        cols = []
        for i in range(l):
            columns = []
            for j in grid:
                columns.append(j[i])
            cols.append(columns)
        col_max = [max(i) for i in cols]
        row_max = [max(i) for i in grid]
        res = 0
        for i in range(l):
            for j in range(l):
               res += min(row_max[i],col_max[j]) - grid[i][j]
        return res


if __name__ == "__main__":
    func = Solution().maxIncreaseKeepingSkyline
    # nums = [[1, 2, 3, 4], [4, 5, 6, 7], [8, 9, 10, 11], [11, 12, 13, 14]]
    grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
    print(func(grid))
