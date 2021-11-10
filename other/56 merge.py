from typing import List
from pysnooper import snoop


class Solution:
    # @snoop()
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        res = [intervals[0]]
        pre_min = intervals[0][0]
        pre_max = intervals[0][1]
        for i in intervals[1:]:
            if pre_min <= i[0] <= pre_max:
                res.pop()
                pre_min = min(pre_min, i[0])
                pre_max = max(pre_max, i[1])
                res.append([pre_min, pre_max])
            else:
                res.append([i[0], i[1]])
                pre_min = i[0]
                pre_max = i[1]
        return res


if __name__ == '__main__':
    sol = Solution().merge
    print(sol([[1, 3], [2, 6], [8, 10], [15, 18]]))
    print(sol([[1, 4], [4, 5]]))
    print(sol([[1, 4], [0, 4]]))
    print(sol([[1, 5], [2, 3]]))
    print(sol([[1, 4], [0, 0]]))
