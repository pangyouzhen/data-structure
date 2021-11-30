from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        soretd_list = sorted(heights)
        res = 0
        for i, v in zip(soretd_list, heights):
            if i != v:
                res += 1
        return res
