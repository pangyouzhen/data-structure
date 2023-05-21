from typing import List


class Solution:
    def similarPairs(self, words: List[str]) -> int:
        l = len(words)
        n = 0
        for i in range(l):
            for j in range(i+1,l):
                if set(words[i]) == set(words[j]):
                    n += 1
        return n