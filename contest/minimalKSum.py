from typing import List

# TODO
class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        val = (1 + k) * k / 2
        c = 0
        window = k
        for i in nums:
            if i <= k:
                val = val - i
                c += 1
                if k + c not in nums:
                    pass