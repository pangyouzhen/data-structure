class Solution:
    def lengthOfLastWord(self, s):
        print(s.split(" ")[-1])
        print("------")
        return len(s.split(" ")[-1])


if __name__ == '__main__':
    sol = Solution().lengthOfLastWord
    assert sol("Hello world") == 5
    assert sol("a ") == 0
