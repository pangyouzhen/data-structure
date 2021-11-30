from typing import List


class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        res = float('inf')
        for i, v in enumerate(nums):
            if v == target:
                val_ = abs(i - start)
                if val_ < res:
                    res = val_
        return res


if __name__ == '__main__':
    nums = [1]
    target = 1
    start = 0
    sol = Solution()
    print(sol.getMinDistance(nums, target, start))
