from typing import List


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        min_val = nums[0] * nums[1]
        max_val = nums[-2] * nums[-1]
        return max_val - min_val
