from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        res = [0] * len(nums)
        res[0] = nums[0]
        for i in range(1, len(nums)):
            res[i] = res[i - 1] + nums[i]
        min_val = min(res)
        if min_val >= 0:
            return 1
        else:
            return -min_val + 1
