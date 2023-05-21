from collections import Counter
from typing import List


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        c1 = Counter(words1)
        c2 = Counter(words2)
        ks = c1.keys() & c2.keys()
        res = []
        if ks:
            for i in ks:
                if c1[i] == 1 and c2[i] == 1:
                    res.append(i)
        return len(res)


if __name__ == "__main__":
    func = Solution().countWords
    words1 = ["leetcode","is","amazing","as","is"]
    words2 = ["amazing","leetcode","is"]
    print(func(words1,words2))
