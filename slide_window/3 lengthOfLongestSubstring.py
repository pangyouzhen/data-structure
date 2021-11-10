#  这个题目的考点是滑动窗口
from pysnooper import snoop


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

    def lengthOfLongestSubstring2(self, s):
        occ = set()
        n = len(s)
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                occ.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1] not in occ:
                occ.add(s[rk + 1])
                rk += 1
            ans = max(ans, rk - i + 1)
        return ans

    # 暴力解法
    # @snoop()
    def lengthOfLongestSubstring3(self, s: str):
        l = len(s)
        _ = 0
        for i in range(l):
            for j in range(i, l + 1):
                if len(set(s[i:j])) == len(s[i:j]):
                    if len(s[i:j]) > _:
                        _ = len(s[i:j])
        return _


if __name__ == '__main__':
    sol = Solution().lengthOfLongestSubstring3
    assert sol("abcabcbb") == 3
    assert sol("bbbbb") == 1
    assert sol("pwwkew") == 3
    assert sol("pwwkewc") == 4
    assert sol("abcadec") == 5
