class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        m = len(s)
        n = len(t)
        if m > n:
            return False
        low = 0
        fast = 0
        ans = False
        while low < m and fast < n:
            if s[low] == t[fast]:
                low += 1
                fast += 1
            else:
                fast += 1
            #   这个问题的关键是什么时候终止  low ==m
            if low == m:
                return True
        return ans
