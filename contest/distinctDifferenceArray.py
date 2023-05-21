from typing import List


class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = []
        for i in range(1,l):
            left = nums[:i]
            right = nums[i:]
            s = len(set(left)) - len(set(right))
            res.append(s)
        return res