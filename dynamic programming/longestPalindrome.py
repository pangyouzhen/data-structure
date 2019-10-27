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


if __name__ == '__main__':
    sol = Solution()
    assert sol.longestPalindrome("a") == "a"
    assert sol.longestPalindrome("ac") == "a"
    assert sol.longestPalindrome("babad") == "bab"
    assert sol.longestPalindrome("cbba") == "bb"
    assert sol.longestPalindrome("ccc") == "ccc"
    assert sol.longestPalindrome("") == ""
# 中心对称，轴对称
# DP
