from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = -1
        for i in nums:
            if i > 0 and -i in nums_set:
                if i > res:
                    res = i
        return res