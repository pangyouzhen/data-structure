class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        n = len(s)
        dp = [1] * n
        for i in range(1, n):
            if ord(s[i]) - ord(s[i - 1]) == 1:
                dp[i] = dp[i - 1] + 1
        return max(dp)
