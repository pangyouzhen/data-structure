from typing import List


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        init_val = float("inf")
        res = None
        for n in nums:
            if abs(n) < init_val:
                init_val = abs(n)
                res = n
            elif abs(n) == init_val:
                res = max(n,res)
        return res 