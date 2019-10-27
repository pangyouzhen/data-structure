class Solution:
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0


if __name__ == '__main__':
    sol = Solution().lengthOfLongestSubstring
    assert sol("abcabcbb") == 3
    assert sol("bbbbb") == 1
    assert sol("pwwkew") == 3
    assert sol("pwwkewc") == 4
    assert sol("abcadec") == 5