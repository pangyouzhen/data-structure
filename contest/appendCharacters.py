class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        l = len(s)
        r = len(t)
        left = 0
        right = 0
        while left < l and right < r:
            if s[left] != t[right]:
                left += 1
            elif s[left] == t[right]:
                left += 1
                right += 1
        return len(t[right:])

if __name__ == "__main__":
    func = Solution().appendCharacters
    s = "coaching"
    t = "coding"
    print(func(s,t))