class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_val, start = 0, -1
        map = {}
        for i in range(len(s)):
            char = s[i]
            if char in map.keys():
                start = max(start, map[char])
            map[char] = i
            max_val = max(max_val, i - start)
        return max_val


if __name__ == '__main__':
    s = "au"
    sol = Solution()
    print(sol.lengthOfLongestSubstring(s))
