class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        n = len(s)
        left = right = 0
        maxn = 0
        while right < n:
            while s[right] in window:
                window.remove(s[left])
                left += 1

            window.add(s[right])
            maxn = max(maxn, right - left + 1)
            right += 1
        return maxn


if __name__ == '__main__':
    s = "abcabcbb"
    sol = Solution()
    print(sol.lengthOfLongestSubstring(s))
