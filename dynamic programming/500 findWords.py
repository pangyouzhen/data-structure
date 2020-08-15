from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        words_dict = {}
        ones = "qwertyuiop"
        words_dict.update({i: 1 for i in ones})
        twos = "asdfghjkl"
        words_dict.update({i: 2 for i in twos})
        threes = "zxcvbnm"
        words_dict.update({i: 3 for i in threes})
        res = []

        for i in words:
            t = True
            start = 0
            l = ""
            word_lower = i.lower()
            while start < len(word_lower):
                if not l:
                    l = words_dict[word_lower[start]]
                    start += 1
                elif words_dict[word_lower[start]] == l:
                    start += 1
                else:
                    t = False
                    break
            if t == True:
                res.append(i)

        return res


if __name__ == '__main__':
    sol = Solution()
    res = sol.findWords(["Hello", "Alaska", "Dad", "Peace"])
    print(res)
