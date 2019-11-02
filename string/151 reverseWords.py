class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(list(filter(lambda x:len(x) >= 1,s.split(" ")))[::-1])


if __name__ == '__main__':
    sol = Solution()
    assert sol.reverseWords("the sky is blue") == "blue is sky the"
    assert sol.reverseWords("  hello world!  ")== "world! hello"
    assert sol.reverseWords("a good   example") == "example good a"
