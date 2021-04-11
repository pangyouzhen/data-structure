from typing import List
import time


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(set(timePoints)) != len(timePoints):
            return 0
        min_val = float('inf')
        time_ls = []
        for i in timePoints:
            time_ls.append(time.mktime(time.strptime(i, "%H:%M")))
            time_ls.append(time.mktime(time.strptime("1900-01-02 %s" % i, "%Y-%m-%d %H:%M")))
        time_ls.sort()
        for i in range(1, len(time_ls)):
            minus_val = time_ls[i] - time_ls[i - 1]
            if minus_val < min_val:
                min_val = minus_val
        return int(min_val / 60)


if __name__ == '__main__':
    a = ["23:59", "00:00"]
    sol = Solution()
    print(sol.findMinDifference(a))
