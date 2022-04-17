from typing import List
from collections import Counter
from math import ceil

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        c = Counter(tasks)
        res = 0
        for k,v in c.items():
            if v < 2:
                return -1
            elif v == 2 or v == 3:
                res += 1
            else:
                res += ceil(v / 3)
        return res
            