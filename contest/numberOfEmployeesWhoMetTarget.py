from typing import List
class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        res = 0
        for i,v in enumerate(hours):
            if v >= target:
                res += 1
        return res