from typing import List
from pysnooper import snoop


class Solution:
    # @snoop()
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        res = 0
        for i in range(1, len(timeSeries)):
            should_duration = timeSeries[i] - timeSeries[i - 1]
            res += min(should_duration, duration)
        res += duration
        return res


if __name__ == '__main__':
    func = Solution().findPoisonedDuration
    # timeSeries = [1, 4]
    # duration = 2
    timeSeries = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    duration = 1
    print(func(timeSeries, duration))
