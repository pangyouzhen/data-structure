class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindrome = ""
        for i in range(len(s)):
            len1 = len(self.getlongestPalindrome(s, i, i))

            if len1 > len(palindrome):
                palindrome = self.getlongestPalindrome(s, i, i)

            len2 = len(self.getlongestPalindrome(s, i, i + 1))
            if len2 > len(palindrome):
                palindrome = self.getlongestPalindrome(s, i, i + 1)

        return palindrome

    def getlongestPalindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1: r]


class Solution2:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = ""
        # 枚举子串的长度 l+1
        for l in range(n):
            # 枚举子串的起始位置 i，这样可以通过 j=i+l 得到子串的结束位置
            for i in range(n):
                j = i + l
                if j >= len(s):
                    break
                if l == 0:
                    dp[i][j] = True
                elif l == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
                if dp[i][j] and l + 1 > len(ans):
                    ans = s[i:j + 1]
        return ans


if __name__ == '__main__':
    sol = Solution()
    assert sol.longestPalindrome("a") == "a"
    assert sol.longestPalindrome("ac") == "a"
    assert sol.longestPalindrome("babad") == "bab"
    assert sol.longestPalindrome("cbba") == "bb"
    assert sol.longestPalindrome("ccc") == "ccc"
    assert sol.longestPalindrome("") == ""
    assert sol.longestPalindrome("abccccdd") == '7'
# 中心对称，轴对称
# DP
