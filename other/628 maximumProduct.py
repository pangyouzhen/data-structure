from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        val = nums[-3] * nums[-2] * nums[-1]
        if nums[0] < 0 < nums[-1] and nums[1] < 0:
            temp = nums[0] * nums[1] * nums[-1]
            val = max(val, temp)
        return val
