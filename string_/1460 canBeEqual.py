from typing import List
from collections import Counter


class Solution:
    def canBeEqual(self, arr: List[int], pieces: List[int]) -> bool:
        c1 = Counter(arr)
        c2 = Counter(pieces)
        if c1 == c2:
            return True
        return False
