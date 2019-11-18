from typing import List
from functools import reduce, lru_cache


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pass


if __name__ == '__main__':
    sol = Solution()
    assert sol.generate(5) == \
           [
               [1],
               [1, 1],
               [1, 2, 1],
               [1, 3, 3, 1],
               [1, 4, 6, 4, 1]
           ]
