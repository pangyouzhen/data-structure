import re


class Solution:

    def numDifferentIntegers(self, word: str) -> int:
        res = [int(i) for i in re.split("\D+", word) if i]
        return len(set(res))


if __name__ == '__main__':
    word = "leet1234code234"
    sol = Solution()
    print(sol.numDifferentIntegers(word))
