from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        res = 0
        for i in arr1:
            t = True
            for j in arr2:
                if abs(i - j) <= d:
                    t = False
                    break
            if t:
                res += 1
        return res