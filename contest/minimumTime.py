import heapq
from typing import List
import math


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        if len(time) == 1:
            return time[0] * totalTrips
        last = time[0]
        gcb_val = None
        for i in range(1, len(time)):
            gcb_val = math.gcd(last, time[i])
            last = int(last * time[i] / gcb_val)
        lcm = last
        coff = 0
        for i in time:
            coff += lcm / i
        res = math.ceil(totalTrips * lcm / coff)
        if res % gcb_val == 0:
            return res
        elif int(res / coff) == 0:
            time.sort()
            return time[totalTrips - 1]
        else:
            pass

if __name__ == '__main__':
    # time = [1, 2, 3]
    # totalTrips = 5
    time2 = [5, 10, 10]
    totalTrips2 = 9
    sol = Solution()
    # print(sol.minimumTime(time, totalTrips))
    print(sol.minimumTime(time2, totalTrips2))
    # assert sol.minimumTime(time2, totalTrips2) == 25
    nums = [9, 3, 10, 5]
    func = Solution().minimumTime
    print(func(nums, 2))
    time3 = [3, 3, 8]
    totalTrips3 = 6
    print(func(time3, totalTrips3))
