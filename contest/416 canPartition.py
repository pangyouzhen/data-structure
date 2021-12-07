from typing import List
from pysnooper import snoop

# todo
class Solution:
    # @snoop()
    # 不是左右双指针,比如[1,1,2,2], 比如[2,2,1,1]
    # 就是从m个数字来任取n个能否等于指定的某个值, 深度优先搜索/ 回溯等等
    def canPartition(self, nums: List[int]) -> bool:
        l = len(nums)
        if l == 1:
            return False
        s = sum(nums)
        if s % 2 == 1:
            return False
        mid = int(s / 2)
        a = self.dfs_(nums, 0, mid)
        return a

    @snoop()
    def dfs_(self, nums: List[int], t: int, target: int) -> bool:
        if target == 0:
            return True
        elif target < 0 or t == len(nums):
            return False
        for i in range(t, len(nums)):
            target -= nums[i]
            if self.dfs_(nums, t + 1, target) is True:
                return True
            target += nums[i]


if __name__ == '__main__':
    sol = Solution()
    func = sol.canPartition
    # nums = [1, 5, 11, 5]
    # nums = [1, 3, 4, 4]
    # nums = [2, 2, 1, 1]
    nums = [1, 2, 5]
    # print(func(nums, 0, 3))
    print(func(nums))
