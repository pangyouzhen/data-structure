from typing import List


# TODO
class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        ranges.sort()
        
        cnt = 1
        right = -1
        l = len(ranges)
        for i in range(l):
            pass