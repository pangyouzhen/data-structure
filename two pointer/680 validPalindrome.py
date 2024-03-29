class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(low, high):
            i, j = low, high
            while i < j:
                if s[i] != s[j]:
                    return False
                i = i + 1
                j = j - 1
            return True

        low, high = 0, len(s) - 1
        while low < high:
            if s[low] == s[high]:
                low = low + 1
                high = high - 1
            else:
                return checkPalindrome(low + 1, high) or checkPalindrome(low, high - 1)
        return True


sol = Solution()
print(sol.validPalindrome("abca"))
assert sol.validPalindrome("abca") == True
print(sol.validPalindrome("abcca"))
