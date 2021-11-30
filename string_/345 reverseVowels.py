class Solution:
    def reverseVowels(self, s: str) -> str:
        left, right = 0, len(s) - 1
        s = list(s)
        #
        while left < right:
            if s[left] in "aeiouAEIOU":
                while s[right] not in "aeiouAEIOU":
                    right -= 1
                s[left], s[right] = s[right], s[left]
                right -= 1
            left += 1

        return ''.join(s)

if __name__ == '__main__':
    sol = Solution()
    assert sol.reverseVowels("hello") == "holle"
    assert sol.reverseVowels("leetcode") == "leotcede"
