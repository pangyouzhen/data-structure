class Solution:
    def isPalindrome(self, s: str, start, end):
        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return False
        return True

    # 暴力解法
    def longestPalindrome2(self, s: str) -> str:
        n = len(s)
        best = ""
        for i in range(n):
            for j in range(i, n):
                if j - i + 1 > len(best) and self.isPalindrome(s, i, j):
                    best = s[i:j + 1]
        return best

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
    func = sol.longestPalindrome2
    assert func("a") == "a"
    assert func("ac") == "a"
    assert func("babad") == "bab"
    assert func("cbba") == "bb"
    assert func("ccc") == "ccc"
    assert func("") == ""
    assert func("abccccdd") == 'cccc'
