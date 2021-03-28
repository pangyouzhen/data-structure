import string
import re


class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        # return re.split("[\w+]", word)
        res = [[]]
        result = []
        for i in word:
            if i.isdigit():
                res[-1].extend(i)
            else:
                res.append([])
        for i in res:
            if i:
                l = int("".join(i))
                result.append(l)
        return len(set(result))




if __name__ == '__main__':
    word = "leet1234code234"
    sol = Solution()
    print(sol.numDifferentIntegers2(word))
