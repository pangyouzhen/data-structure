from typing import List

# TODO
class Solution:
    def minNumber(self, nums: List[int]) -> str:
        max_val = max(nums)
        l = len(str(max_val))
        n = []
        for i in nums:
            tmp = str(i)
            if len(tmp) < l:
                tmp += "0" * (l - len(str))
            n.append(tmp)
        n.sort()
        