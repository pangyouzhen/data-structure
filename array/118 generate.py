from typing import List
from collections.abc import __all__
from functools import lru_cache


class Solution:
    def compute(self, ls: List) -> List:
        return [1] + [ls[i] + ls[i + 1] for i in range(len(ls) - 1)] + [1]

    @lru_cache()
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        t = []
        if numRows == 1:
            t.append([1])
        elif numRows == 2:
            t.append([1])
            t.append([1, 1])
        else:
            t = self.generate(numRows - 1)
            t.append(self.compute(t[-1]))
        return t


if __name__ == '__main__':
    sol = Solution()
    print(sol.generate(1))
    print(sol.generate(2))
    print(sol.generate(5))
    # assert sol.generate(5) == \
    #        [
    #            [1],
    #            [1, 1],
    #            [1, 2, 1],
    #            [1, 3, 3, 1],
    #            [1, 4, 6, 4, 1]
    #        ]
