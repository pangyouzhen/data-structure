class Solution:
    def countKeyChanges(self, s: str) -> int:
        s = s.lower()
        prev = s[0]
        res = 0
        for i in s:
            if i == prev:
                continue
            else:
                prev = i
                res += 1
        return res