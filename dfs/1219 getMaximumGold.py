from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        # 上下左右
        dircection = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        res = 0
        for i,v in enumerate(grid):
            for j,ind2 in enumerate(v):
               pass



if __name__ == "__main__":
    func = Solution().getMaximumGold
    nums = []
    print(func(nums))
