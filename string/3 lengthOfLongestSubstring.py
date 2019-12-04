class Solution:
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        used = {}
        max_legth = start = 0
        for i, c in enumerate(s):
            if c in used and start <= used[c]:
                start = used[c] + 1
            else:
                max_legth = max(max_legth, i - start + 1)
            used[c] = i
        return max_legth


if __name__ == '__main__':
    sol = Solution().lengthOfLongestSubstring
    assert sol("abcabcbb") == 3
    assert sol("bbbbb") == 1
    assert sol("pwwkew") == 3
    assert sol("pwwkewc") == 4
    assert sol("abcadec") == 5
