from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ones = set("qwertyuiop")
        twos = set("asdfghjkl")
        threes = set("zxcvbnm")
        res = []
        for word in words:
            word_set = set(word.lower())
            if word_set <= ones or word_set <= twos or word_set <= threes:
                res.append(word)
        return res


if __name__ == '__main__':
    sol = Solution()
    res = sol.findWords(["Hello", "Alaska", "Dad", "Peace"])
    print(res)
