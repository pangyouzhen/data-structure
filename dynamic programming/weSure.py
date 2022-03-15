#  [6,7,9,10,11,4,5,6,7] 中长度大于3以上的等差子序列能组成的总个数
# [6,7,9,10,11,4,5,6,7] -> [1,2,1,1,-7,1,1,1]
#  9,10,11 和 4,5,6,7
from typing import List


class Solution:
    # TODO
    def total_minum(self, nums: List) -> int:
        if len(nums) <= 2:
            return 0
        n = len(nums)
        dp = [0] * (n + 1)
        minum = [0] * n
        temp = float("-inf")
        minum[0] = nums[1] - nums[0]
        for i in range(2, n + 1):
            minum[i - 1] = nums[i] - nums[i - 1]
            if minum[i - 1] == temp:
                temp += 1
            if temp >= 2:
                pass
            else:
                continue
