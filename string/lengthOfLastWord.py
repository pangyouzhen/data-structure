class Solution:
    def lengthOfLastWord(self, s):
        if s.strip():
            return len(s.split()[-1])
        return 0


if __name__ == '__main__':
    sol = Solution().lengthOfLastWord
    assert sol("Hello world") == 5
    assert sol("a ") == 1
    assert sol(" ") == 0
