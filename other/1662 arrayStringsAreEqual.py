from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w1 = "".join(word1)
        w2 = "".join(word2)
        if w1 == w2:
            return True
        return False


if __name__ == '__main__':
    word1 = ["a", "cb"]
    word2 = ["ab", "c"]
    sol = Solution()
    print(sol.arrayStringsAreEqual(word1, word2))
