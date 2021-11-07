from typing import List
from pysnooper import snoop


class Solution:
    # @snoop()
    # todo
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        pre_min = intervals[0][0]
        pre_max = intervals[0][1]
        if len(intervals) == 1:
            res.append([pre_min, pre_max])
        for i in intervals[1:]:
            if i[0] <= pre_max:
                res.append([pre_min, i[1]])
                pre_max = i[1]
            else:
                res.append([pre_min, pre_max])
                res.append([i[0], i[1]])
                pre_min = i[0]
                pre_max = i[1]
        return res


if __name__ == '__main__':
    sol = Solution().merge
    print(sol([[1, 3], [2, 6], [8, 10], [15, 18]]))
    # print(sol([[1, 4], [5, 6]]))
