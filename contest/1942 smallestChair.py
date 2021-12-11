from typing import List


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        t = times[targetFriend]
        start = t[0]
        end = t[1]
        times.pop(targetFriend)
        sort_time = sorted(times, key=lambda x: x[0])
        res = 0
        prev_start = sort_time[0][0]
        prev_end = sort_time[0][1]
        if prev_start == start:
            return res
        for i in sort_time[1:]:
            if prev_start
