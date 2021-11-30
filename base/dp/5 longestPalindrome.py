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
    def longestPalindrome2(self, s: str) -> str:
        pass


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
