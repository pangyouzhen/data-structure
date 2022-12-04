from typing import List

# TODO
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        s = sum(arr)
        q,t = divmod(s,3)
        if t != 0:
            return False
        tmp = 0
        n = 0
        for i in arr:
            tmp += i
            if tmp == q:
                tmp = 0
                n += 1
        return tmp == 0 and n == 3
        