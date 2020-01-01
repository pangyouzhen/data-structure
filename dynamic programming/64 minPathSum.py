from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        return self.uniquePath(0, 0, grid)

    def uniquePath(self, param, param1, grid):
        if param < 0 or param1 < 0:
            return 0
        else:
            return min(self.uniquePath(param - 1, param1, grid) + grid[param][param1],
                       self.uniquePath(param, param1 - 1, grid) + grid[param][param1])


# f(i,j) = min(f(x-1,j)+k,f(j-1,i)+k)
if __name__ == '__main__':
    ls = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    sol = Solution()
    print(sol.minPathSum(ls))
