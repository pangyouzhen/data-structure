from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # 滑动窗口，肯定超时
        # 前缀和
        res = 0
        for i in range(len(nums) - k + 1):
            t = nums[i:i + k]
            if len(t) == set(t):
                s = sum(t)
                res = max(s, res)
        return res
