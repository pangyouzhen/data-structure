from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        fst_col = max(points[0])