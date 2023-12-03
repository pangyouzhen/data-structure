from typing import List

class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        s = sum(arr)
        q,t = divmod(s,3)
        if t != 0:
            return False
        vals = 0
        pass