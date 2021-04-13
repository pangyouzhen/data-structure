class Solution:
    def longest_str(self, s):
        dp = [0] * len(s)
        dp[0] = 1
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                dp[i] += 1
            else:
                dp[i] = dp[i - 1] + 1
        max_val = max(dp)
        ind = dp.index(max_val)
        return s[ind] * int(max_val)


if __name__ == '__main__':
    s = "abbbbcccddddddddeee"
    sol = Solution()
    print(sol.longest_str(s))