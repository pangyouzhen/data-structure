from typing import List
from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = Counter(arr)
        key_num = len(c)
        val_num = list(c.values())
        if len(set(val_num)) != key_num:
            return False
        return True
