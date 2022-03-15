class Solution:
    # TODO
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        if n % 2 == 0:
            pass
        else:
            mid = n // 2
            left = mid - 1
            right = mid + 1
