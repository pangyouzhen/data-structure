
from typing import List


class Solution:
    def knap(self, w: List[int], v: List[int], c: int):
        pass
        n = len(w)
        self.knap02(w, v, n, c) = max(
            self.knap02(w, v, n-1, c),
            v[i] + self.knap02(w, v, n-1, c-w[i])
        )

    def knap02(self, w: List[int], v: List[int], index: int, c: int):
