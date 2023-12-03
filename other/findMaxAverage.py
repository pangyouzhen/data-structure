from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = sum(nums[:k])
        l = len(nums)
        res = s
        for i in range(l-k):
            v = s - nums[i] + nums[i+k]
            s = v
            res = max(res,s)
        return s / k