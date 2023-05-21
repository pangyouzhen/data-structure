import itertools
from typing import List


class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # grid[0:3]
        # for i in grid[0:3]
        # for i in grid[1:4]
        res = 0
        for i in range(0, m - 2):
            # print(grid[i:i + 3])
            v: List[List[int]] = grid[i:i + 3]
            # a = []
            for k in range(0, n - 2):
                a = []
                for j in v:
                    a.append(j[k:k + 3])
                s = sum(itertools.chain.from_iterable(a))
                s = s - a[1][0] - a[1][-1]
                if s > res:
                    res = s
            # print(a)
        return res


if __name__ == '__main__':
    func = Solution().maxSum
    grid = [[6, 2, 1, 3], [4, 2, 1, 5], [9, 2, 8, 7], [4, 1, 2, 9]]
    print(func(grid))
