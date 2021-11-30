from typing import List
from collections import Counter


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        res = []
        for k, v in c.items():
            if int(v) == 1:
                res.append(k)
        return res
