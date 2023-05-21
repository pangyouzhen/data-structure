from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        l = len(intervals)
        ans = 0

        def overlap(left: List[List[int]], right: List[List[int]]):
            if left[1] > right[0]:
                return True
            return False

        for i in range(1, l):
            if overlap(intervals[i - 1], intervals[i]):
                intervals[i][1] = min(intervals[i - 1][1], intervals[i][1])
                ans += 1
        return ans
