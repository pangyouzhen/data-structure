from collections import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        c = Counter(s)
        res = 0
        for a, v in c.items():
            if v % 2 == 1:
                res += 1
        if res > k:
            return False
        return True
