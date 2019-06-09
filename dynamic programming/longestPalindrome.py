class Solution:
    def longestPalindrome(self, s: str) -> str:
        pass

    def is_palindrome(self, s):
        if list(s) == list(s)[::-1]:
            return True
        else:
            return False


if __name__ == '__main__':
    pass
