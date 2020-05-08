import collections
from functools import reduce


class Solution(object):
    def longestWord(self, words):
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()
        END = True

        for i, word in enumerate(words):
            reduce(dict.__getitem__, word, trie)[END] = i
        return trie


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestWord(["hello", "word"]))
