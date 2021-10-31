from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ones = "qwertyuiop"
        twos = "asdfghjkl"
        threes = "zxcvbnm"
        keys = [set(ones), set(twos), set(threes)]
        res = []
        for word in words:
            word_set = set(word.lower())
            r = [True for k in keys if k & word_set]
            if len(r) == 1:
                res.append(word)
        return res


if __name__ == '__main__':
    sol = Solution()
    res = sol.findWords(["Hello", "Alaska", "Dad", "Peace"])
    print(res)
