from typing import List
from pysnooper import snoop


# todo
class Solution:
    # @snoop()
    # 不是左右双指针,比如[1,1,2,2], 比如[2,2,1,1]
    # 就是从m个数字来任取n个能否等于指定的某个值, 深度优先搜索/ 回溯等等
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0:
            return False
        return self.try_partiton(nums, len(nums) - 1, s/2)

    def try_partiton(self, nums, ind, s):
        if s == 0:
            return True
        if s < 0 or ind < 0:
            return False
        return  self.try_partiton(nums,ind-1,s) or self.try_partiton(nums,ind-1,s-nums[ind]) 


if __name__ == '__main__':
    sol = Solution()
    func = sol.canPartition
    # nums = [1, 5, 11, 5]
    # nums = [1, 3, 4, 4]
    # nums = [2, 2, 1, 1]
    nums = [1, 2, 5]
    # print(func(nums, 0, 3))
    print(func(nums))
