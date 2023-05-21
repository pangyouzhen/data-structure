from typing import List
from collections import defaultdict

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d = defaultdict(int)
        for v in arr:
            d[v] += 1
        c = 0
        for i,v in d.items():
            if v != 1:
                continue
            c += 1
            if c == k:
                return i