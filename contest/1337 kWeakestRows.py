from typing import List
from collections import Counter


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        res = []
        for i, v in enumerate(mat):
            c = Counter(v)[1]
            res.append((i, c))
        s = sorted(res, key=lambda x: x[1])
        s0 = [i[0] for i in s]
        return s0[:k]


if __name__ == '__main__':
    mat = [[1, 1, 0, 0, 0], [1, 1, 1, 1, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 1, 1, 1]]
    func = Solution().kWeakestRows
    assert func(mat, 3)
