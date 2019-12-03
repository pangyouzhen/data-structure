from typing import List
from functools import reduce, lru_cache


class Solution:
    def compute(self, ls: List) -> List:
        return [1] + [ls[i] + ls[i + 1] for i in range(len(ls) - 1)] + [1]

    @lru_cache()
    def getRow(self, numRows: int) -> List[int]:
        res = []
        if numRows == 0:
            res.append(1)
        elif numRows == 1:
            res.append(1)
            res.append(1)
        else:
            t = self.getRow(numRows - 1)
            res = (self.compute(t))
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.getRow(1))
    print(sol.getRow(2))
    print(sol.getRow(3))
    print(sol.getRow(4))
    print(sol.getRow(5))
    # assert sol.getRow(4) == [1, 4, 6, 4, 1]
