from collections import Counter
from typing import List
from pysnooper import snoop


class Solution:
    # @snoop()
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        char = []
        for i in licensePlate:
            if i.isalpha():
                char.append(i.lower())
        c = Counter(char)
        res = []
        for j in words:
            w = Counter(j)
            char_bool = True
            for k, v in c.items():
                if k not in w.keys():
                    char_bool = False
                    break
                if k in w.keys() and v > w[k]:
                    char_bool = False
                    break
            if char_bool:
                res.append(j)
        l = [len(i) for i in res]
        min_l = min(l)
        for t in res:
            if min_l == len(t):
                return t


if __name__ == "__main__":
    sol = Solution().shortestCompletingWord
    # licensePlate = "1s3 PSt"
    # words = ["step", "steps", "stripe", "stepple"]
    # licensePlate = "1s3 456"
    # words = ["looks", "pest", "stew", "show"]
    licensePlate = "Ah71752"
    words = ["suggest", "letter", "of", "husband", "easy", "education", "drug", "prevent", "writer", "old"]
    print(sol(licensePlate, words))
