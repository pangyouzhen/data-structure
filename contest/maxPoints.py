from typing import List


# TODO
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        fst_col = max(points[0])
