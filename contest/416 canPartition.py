from typing import List
from pysnooper import snoop


class Solution:
    # @snoop()
    # 不是左右双指针,比如[1,1,2,2], 比如[2,2,1,1]
    # todo
    def canPartition(self, nums: List[int]) -> bool:
        l = len(nums)
        if l == 1:
            return False
        s = sum(nums)
        if s % 2 == 1:
            return False
        mid = s / 2
        if self.dfs_(nums, 0, mid) is True:
            return True

    def dfs_(self, nums: List[int], t: int, target) -> bool:
        if target == 0:
            return True
        for i in range(t, len(nums)):
            self.dfs_(nums[t:], t, target - nums[i])


if __name__ == '__main__':
    func = Solution().canPartition
    # nums = [1, 5, 11, 5]
    # nums = [1, 3, 4, 4]
    nums = [2, 2, 1, 1]
    print(func(nums))
