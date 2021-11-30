from typing import List
from collections import Counter


class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        str_counter = Counter((A + " " + B).split())
        print(str_counter)
        return [i for i, v in str_counter.items() if v == 1]


if __name__ == '__main__':
    A = "this apple is sweet"
    B = "this apple is sour"
    sol = Solution()
    print(sol.uncommonFromSentences(A, B))
