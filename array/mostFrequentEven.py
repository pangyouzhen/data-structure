from typing import List
from collections import Counter, defaultdict


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        c = Counter(nums)
        a = defaultdict(list)
        for i, v in c.items():
            if i % 2 == 0:
                a[v].append(i)
        if len(a) > 0:
            max_val = max(a.keys())
            return min(a[max_val])
        return -1