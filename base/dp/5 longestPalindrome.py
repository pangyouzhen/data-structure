class Solution:

    # 暴力解法
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(s: str):
            start = 0
            end = len(s) - 1
            while start < end:
                if s[start] == s[end]:
                    start += 1
                    end -= 1
                else:
                    return False
            return True

        n = len(s)
        res = ""
        for i in range(n + 1):
            for j in range(i):
                s_str = s[j:i]
                if isPalindrome(s_str):
                    if len(s_str) > len(res):
                        res = s_str
        return res

    #  非暴力解法
    # TODO
    def longestPalindrome2(self, s: str) -> str:
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
    func = sol.longestPalindrome
    assert func("a") == "a"
    assert func("ac") == "a"
    assert func("babad") == "bab"
    assert func("cbba") == "bb"
    assert func("ccc") == "ccc"
    assert func("") == ""
    assert func("abccccdd") == 'cccc'
